import os
from dotenv import load_dotenv 
from openai import OpenAI
 
load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"),
                base_url=os.getenv("BASE_URL"))

response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {"role": "user", "content": "请用一句话介绍人工智能"}

    ]
)
print(response.choices[0].message.content)