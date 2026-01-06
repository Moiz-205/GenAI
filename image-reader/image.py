import io
import base64
from groq import Groq
from ..config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

default_model = 'meta-llama/llama-4-scout-17b-16e-instruct'

def pil_to_data_url(pil_image, format="JPEG"):
    buffer = io.BytesIO()
    pil_image.save(buffer, format=format)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    mime = format.lower()
    return f"data:image/{mime};base64,{encoded}"

def groq_image(image,prompt,model=default_model):
    system_prompt = '''You are image classifier.'''

    if image is None:
        return 'Please upload an image of animal.'
    if not prompt or not prompt.strip():
        return 'Please enter a prompt.'

    image_data = pil_to_data_url(image)

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": image_data}},
            ],
        }
    ]

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature = 0.2,
            max_completion_tokens = 256,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print('Groq API call error: ', e)
        return "Error processing the image."
