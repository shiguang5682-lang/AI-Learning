from src.config import config

from src.logger import logger

from openai import OpenAI

client = OpenAI(api_key=config.api_key, base_url=config.base_url)

def chat(prompt: str) -> str:
    """向LLM发送一次对话请求并返回回复"""

    logger.info("Sending request to LLM")
    response = client.chat.completions.create(
        model=config.model,
        messages=[
          
            {"role": "user", "content": prompt}
        ],
    )
    logger.info("LLM response received")
    return response.choices[0].message.content or ""
