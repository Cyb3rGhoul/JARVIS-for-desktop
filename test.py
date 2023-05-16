import os
import openai


openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Hi",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0)

print(response)

'''
{
  "choices": [
    {
      "finish_reason": "length",
      "index": 0,
      "logprobs": null,
      "text": ",\n\nI am looking for a good quality, reasonably priced printer for my home office to use for printing documents and occasional photo prints. I want it to be able to print in both color and black and white, and be compatible with both Windows and Mac systems.\n\nOne option is the Epson Expression XP-7100 Small-in-One Printer. This printer offers a variety of features including a fast printing speed of 15 ppm (pages per minute) for both color and black and white documents, a high-resolution printing capability of up to 5760 x 1440 dpi, and a mobile printing option via Wi-Fi and Apple AirPrint. It also has an auto 2-sided printing feature and a 6.1 cm LCD touchscreen for easy navigation. This printer is compatible with both Windows and Mac systems and is reasonably priced at around $100.\n\nAnother option is the Canon PIXMA MG3650 Wireless All-in-One Printer. This printer is also reasonably priced at around $100, and offers a fast printing speed of 9.7 ppm for color and black and white documents, as well as a high-resolution printing capability of up to 4800 x 1200 dpi. It is also compatible with both Windows and Mac systems"
    }
  ],
  "created": 1684151567,
  "id": "cmpl-7GR2t671yC0rVitNzhILf3psuSbg4",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 256,
    "prompt_tokens": 1,
    "total_tokens": 257
  }
}
'''