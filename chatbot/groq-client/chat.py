from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

model = "moonshotai/kimi-k2-instruct-0905"


def ChatAI(message: str, history: list):
    system_prompt = (
    "You are a Astrophysics teacher who explains complex concepts in simple terms."
    "This is for the middle school and highschool students"
    "Tone has to be educational and friendly"
    )

    messages: list = [{"role": "system", "content": system_prompt}]

    for msg in history:
        if msg is not None:
            messages.append(
                {
                    "role": msg.get("role", "user"),
                    "content": msg.get("content", "")
                }
            )

    messages.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=500,
            temperature=0.75
        )

        reply = response.choices[0].message.content
        return reply

    except Exception as e:
        print('Groq API call error: ', e)
