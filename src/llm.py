from src.config import config

from src.logger import logger

from openai import OpenAI

from src.exceptions import LLMError

from src.models.chat_message import ChatMessage

client = OpenAI(api_key=config.api_key, base_url=config.base_url)

def chat(messages: list[ChatMessage]) -> str:
    """向LLM发送一次对话请求并返回回复"""

    logger.info("Sending request to LLM")
    sdk_messages = [message.to_dict() for message in messages]
    try:
        response = client.chat.completions.create(
            model=config.model,
            messages=sdk_messages
        )
    except Exception as e:
        logger.exception("LLM requests failed")
        raise LLMError(str(e))  from e 
     

    logger.info("LLM response received")
    return response.choices[0].message.content or ""
