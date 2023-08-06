import os
from dotenv import load_dotenv
import requests


class gptDataProcesser():
    def __init__(self, prompt, meetings_text):
        """
        Constructs a new object 'gptDataProcesser' that handles requests to Open AI's GPT API
        :param prompt: Prompt to ask GPT
        :param meetings_text: Transcription of a meeting
        """
        self.gpt_prompt = prompt
        self.gpt_meeting_data = meetings_text

    def get_keys(self):
        """
        :return: returns the API keys used for Open AI API
        """
        load_dotenv()
        openai_api_key = os.getenv("OPENAI_KEY")
        return openai_api_key

    def ask_gpt(self, api_key):
        """
        :param api_key: API key used for Open AI API
        :return: returns a meeting minutes of a meeting from the transcription of a meeting that took place
        """
        response = requests.post(url="https://api.openai.com/v1/chat/completions",
                                 json={"model": "gpt-3.5-turbo-16k",
                                       "messages": [{"role": "user",
                                                     "content": self.gpt_prompt + str("\n") + self.gpt_meeting_data}]},
                                 headers={"Content-Type": "application/json",
                                          "Authorization": "Bearer " + str(api_key)})
        r = response.json()
        return str(r["choices"][0]["message"]["content"])
