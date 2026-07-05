from src.llm import chat 

from src.exceptions import LLMError

messages =[
    {

        "role":"user",
        "content":"请用一句话介绍Agent"

    }
]
try:
    answer = chat(messages)
    print(answer)
except LLMError as e:
    print(f"Error: {e}")