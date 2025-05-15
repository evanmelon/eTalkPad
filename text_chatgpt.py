import os
import openai
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

# ====== 設定 OpenAI API 金鑰 ======
client = OpenAI(api_key=os.getenv("API_KEY"))

def chat_with_gpt(user_input):
    response = client.chat.completions.create(
        model="gpt-4",  # 有用 GPT-4 可換成 "gpt-4"
        messages=[
            {"role": "system", "content": "你是一個友善的助理。"},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# def main():
#     print("💬 ChatGPT CLI 模式（輸入 q 結束）")
#     while True:
#         user_input = input("你說：")
#         if user_input.lower() == 'q':
#             print("👋 再見！")
#             break
#         reply = chat_with_gpt(user_input)
#         print("🤖 ChatGPT 回應：", reply)
# 
# if __name__ == "__main__":
#     main()

