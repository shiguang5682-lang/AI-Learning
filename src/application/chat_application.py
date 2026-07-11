from src.llm import chat 

from src.exceptions import LLMError

from src.prompt import build_messages

from src.memory import ConversationMemory


class ChatApplication:
    def __init__(self):
        self.memory = ConversationMemory()
    
    def run(self):
        while True:
            user_input = input("用户：")
            user_input = user_input.strip()
            if user_input.lower() == "exit":
                break
            answer = self.chat(user_input)
            print("AI:",answer)
        

    def chat(self, user_input:str)  -> str:
        """处理一轮对话,返回模型回复"""
        self.memory.add_user_message(user_input)
        try:
            messages = build_messages(self.memory.get_messages())
            answer = chat(messages)
        except LLMError as e:
            raise LLMError(f"LLM请求失败: {str(e)}") 
        
        self.memory.add_assistant_message(answer)
        return answer