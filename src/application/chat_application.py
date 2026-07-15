from src.llm import chat,stream_chat

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
              
            ##answer =  self.chat(user_input)
            ##print("AI",answer)  

            self.stream_chat(user_input)
            


    def chat(self, user_input:str)-> str:
        """处理一轮对话,返回模型回复"""
        self.memory.add_user_message(user_input)
        
        messages = build_messages(self.memory.get_messages())
        answer = chat(messages)
 
        
        self.memory.add_assistant_message(answer)

        return answer
    
    def stream_chat(self, user_input: str) -> str:
        """处理一轮对话,并以流式方式输出模型回复"""
        self.memory.add_user_message(user_input)
        
        messages = build_messages(self.memory.get_messages())

        chunks:list[str] = []

        print("AI:", end="", flush=True)
        stream_response = stream_chat(messages)


        for chunk in stream_response:
            print(chunk, end="", flush=True)
            chunks.append(chunk)

        print()
        
        answer = "".join(chunks)

        self.memory.add_assistant_message(answer)
        return answer
     
    

