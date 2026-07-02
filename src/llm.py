from openai import OpenAI
from src.config import API_KEY, BASE_URL, MODEL

client = OpenAI(api_key=API_KEY, base_url =BASE_URL)

def chat(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
          
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content