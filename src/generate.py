from openai import OpenAI
import os
from dotenv import load_dotenv
from system_prompt import system_prompt

load_dotenv()

openai_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("API_KEY")
)

# Demo messages for unit testing

# prompt = "What is the capital of India"
# messages = [
#     {
#         "role" : "system",
#         "content" : system_prompt
#     },
#     {
#         "role": "user",
#         "content": prompt,
#     }
# ]

def generate_from_llm(messages, model="deepseek/deepseek-chat-v3-0324:free"):
    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print("Error with generating from the LLM")
        return e