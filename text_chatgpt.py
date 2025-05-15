import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class TextChatGPT:
    """
    A simple wrapper for OpenAI's Chat API that maintains conversation history.
    """

    def __init__(self, api_key=None, model="gpt-4", system_prompt=None):
        self.api_key = api_key or os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key must be provided via constructor or API_KEY environment variable"
            )
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.system_prompt = system_prompt or (
            "你是一個友善的助理。"
            "你在輸出文字時要在一開始加上這串文字的心情，心情可以用happy, angry, sad 這三個心情狀態來表示，打完心情後用：來區隔你要講的文字"
        )
        self.messages = [{"role": "system", "content": self.system_prompt}]

    def get_response(self, user_input):
        """
        Send a user message, update history, call API, and return assistant response.
        """
        self.messages.append({"role": "user", "content": user_input})
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages,
        )
        content = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": content})
        return content

    def reset_conversation(self):
        """
        Clear the conversation history, keeping only the system prompt.
        """
        self.messages = [{"role": "system", "content": self.system_prompt}]
