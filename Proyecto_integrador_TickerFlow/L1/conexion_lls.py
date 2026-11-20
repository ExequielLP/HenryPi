import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"],
)

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role": "user", "content": "Explain closures in one paragraph."}],
)

print(response.choices[0].message.content)

client_gemini = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    api_key=os.environ["GEMINI_API_KEY"],
)

response_gemini = client_gemini.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[{"role": "user", "content": "Explain closures in one paragraph."}],
)

print(response_gemini.choices[0].message.content)