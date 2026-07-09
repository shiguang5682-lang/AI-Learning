from __future__ import annotations
from src.models.chat_message import ChatMessage

def build_messages(messages: list[ChatMessage],
                    system_prompt: str |None = None,
                    
                    ) ->list[ChatMessage]:
    """构建Messages列表"""

    result : list[ChatMessage] = []

    if system_prompt:
       result.append(ChatMessage(role="system", content=system_prompt))
 
    result.extend(messages)

    return result
