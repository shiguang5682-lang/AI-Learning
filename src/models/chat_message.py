from __future__ import annotations
from dataclasses import dataclass


@dataclass(slots=True)
class ChatMessage:
    """
    Represents one message exchanged during a conversation."""

    role: str
    content: str

    def to_dict(self) -> dict[str, str]:
        """Convert the message into the SDK dictionary format"""
        return {"role": self.role, "content": self.content} 

    @classmethod    
    def from_dict(cls, data: dict[str, str]) -> ChatMessage:
        """Create a message object from a dictionary"""
        return cls(role=data["role"], content=data["content"])