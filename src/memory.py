from src.models.chat_message import ChatMessage

class ConversationMemory:
    """保存的是当前会话状态,而不是聊天历史,LLM依赖会话记录"""
    
    def __init__(self) -> None:
        self._messages: list[ChatMessage] = []
    
    def add_user_message(self, content: str) -> None:
        """添加用户消息到聊天历史"""
        self._messages.append(ChatMessage(role ="user", content = content))

    def add_assistant_message(self, content: str) -> None:
        """添加助手消息到聊天历史"""
        self._messages.append(ChatMessage(role ="assistant", content = content))

    def add_system_message(self, content: str) -> None:
        """添加系统消息到聊天历史"""
        self._messages.append(ChatMessage(role = "system", content = content))

    def get_messages(self) -> list[ChatMessage]:
        """获取聊天历史"""
        return self._messages.copy()
    
    def get_recent_messages(self, max_messages: int) -> list[ChatMessage]:
        if max_messages <= 0:
            raise ValueError("max_messages must be greater than 0")

        return self._messages[-max_messages:]

    
    def clear(self) -> None:
        """清空聊天历史"""
        self._messages.clear()
    