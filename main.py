import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import datetime
import subprocess
import os


chatStr = ""
def chat(query):
    global chatStr

    print(chatStr)

    openai.api_key = "Your-API-key"

    chatStr += f"Harsh: {query} \n Jarvis: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # todo add try catch in this
    say(response['choices'][0]['text'])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


    with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)

def ai(prompt):
    openai.api_key = "Your-API-key"
    text = f"Response for the prompt : {prompt} \n******\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #todo add try catch in this
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some error has Occurred. Sorry from Jarvis"

if __name__ == '__main__':


    say("Hello I am Jarvis AI.")
    while True:
        print("Listening..")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"], ["chat GPT", "https://chat.openai.com"], ["google", "https://google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir..")
                webbrowser.open(site[1])

        if "open spotify".lower() in query.lower():
            say("opening spotify sir..")
            file_path = r"C:\Users\Asus\OneDrive\Desktop\Spotify.lnk"
            subprocess.Popen(file_path, shell=True)

        elif "open microsoft team".lower() in query.lower():
            say("opening Microsoft teams sir..")
            file_path = r"C:\Users\Asus\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams (work or school).lnk"
            subprocess.Popen(file_path, shell=True)

        elif "the time".lower() in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} bajke {min} minutes")

        elif"using intelligence".lower() in query.lower():
            ai(prompt=query)

        elif"exit".lower() in query.lower():
            exit()

        elif"reset chat".lower() in query.lower():
            chatStr = ""

        else:
            chat(query)


        # say(query)



