from config import MODEL_NAME
from client import get_client

client = get_client()

messages = [
    {"role": "system", "content": "You are a helpful QnA assistant."}
]

def ask(question: str) -> str:
    messages.append({"role": "user", "content": question})

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=0.2,
        top_p=0.9
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})

    return reply
