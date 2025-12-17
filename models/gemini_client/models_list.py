import google.generativeai as genai
from config import GEMNI_API_KEY

genai.configure(api_key=GEMNI_API_KEY)

models = genai.list_models()

for m in models:
    print(m.id)
