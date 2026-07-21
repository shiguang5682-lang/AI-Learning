from src.llm import chat,stream_chat

from src.exceptions import LLMError

from src.prompt import build_messages

from src.memory import ConversationMemory

from src.models.chat_message import ChatMessage


class ChatApplication:
    def __init__(self,
                 max_context_messages: int = 10,
                 ) -> None:
        self.memory = ConversationMemory()
        self._max_context_messages = max_context_messages

    def _build_messages_for_user_input(self, 
                                       user_input:str,
                                       ) -> list[ChatMessage]:

        self.memory.add_user_message(user_input)
        recent_messages = self.memory.get_recent_messages(self._max_context_messages)

        return build_messages(recent_messages)
    
    def run(self):
        while True:
            user_input = input("用户：")
            user_input = user_input.strip()
            if user_input.lower() == "exit":
                break
              
            ##answer =  self.chat(user_input)
            ##print("AI",answer)  

            self.stream_chat(user_input)
            


    def chat(self, user_input:str) -> str:
        """处理一轮对话,返回模型回复"""
        messages = self._build_messages_for_user_input(user_input)
        
        answer = chat(messages)
 
        
        self.memory.add_assistant_message(answer)

        return answer
    
    def stream_chat(self, user_input: str) -> str:
        """处理一轮对话,并以流式方式输出模型回复"""

        
        messages = self._build_messages_for_user_input(user_input)

        chunks: list[str] = []

        print("AI:", end="", flush=True)
        stream_response = stream_chat(messages)


        for chunk in stream_response:
            print(chunk, end="", flush=True)
            chunks.append(chunk)

        print()
        
        answer = "".join(chunks)

        self.memory.add_assistant_message(answer)
        return answer
     
    

