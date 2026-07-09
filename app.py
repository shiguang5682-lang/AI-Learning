from src.llm import chat 

from src.exceptions import LLMError

from src.prompt import build_messages

from src.memory import ConversationMemory

'''
messages = build_messages(user_prompt="请用一句话介绍Agent"
                          
                          )

try:
    answer = chat(messages)
    print(answer)
except LLMError as e:
    print(f"Error: {e}")
'''
memory = ConversationMemory()

while True:
    user_input = input("用户: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    memory.add_user_message(user_input)
    answer = chat(memory.get_messages())
    print("AI", answer)
    memory.add_assistant_message(answer)