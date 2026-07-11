from typing import Iterator
from src.config import config

from src.logger import logger

from openai import OpenAI

from src.exceptions import LLMError

from src.models.chat_message import ChatMessage

client = OpenAI(api_key=config.api_key, base_url=config.base_url)

def _build_sdk_messages(messages: list[ChatMessage]) -> list[dict]:
    """将ChatMessage对象列表转换为SDK消息字典列表"""
    return [message.to_dict() for message in messages]

def chat(messages: list[ChatMessage]) -> str:
    """向LLM发送一次对话请求并返回回复"""

    logger.info("Sending request to LLM")
    sdk_messages = _build_sdk_messages(messages)
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

def stream_chat(messages: list[ChatMessage]) -> Iterator[str]:
    """向LLM发送一次对话请求并返回流式回复"""

    logger.info("Sending request to LLM")
    sdk_messages = _build_sdk_messages(messages)
    try:
        response = client.chat.completions.create(
            model=config.model,
            messages=sdk_messages,
            stream=True
        )
    except Exception as e:
        logger.exception("LLM requests failed")
        raise LLMError(str(e))  from e
    logger.info("LLM response received")
    for chunk in response:
        if chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content

