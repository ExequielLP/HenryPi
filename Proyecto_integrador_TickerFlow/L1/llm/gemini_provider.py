"""
ADAPTADOR para Gemini (Google): usa la API compatible con OpenAI de Google.
Por fuera se ve igual que GroqProvider: summarize(ticket) -> dict.
"""

import json
import os

from openai import OpenAI

from llm.base import INSTRUCCIONES, Provider


class GeminiProvider(Provider):
    def __init__(self):
        self.client = OpenAI(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=os.environ["GEMINI_API_KEY"],
            max_retries=0,  # los reintentos los maneja nuestro llm/retry.py
        )
        # Si da error 404, revisa el nombre exacto del modelo en Google AI Studio.
        self.model = "gemini-3.7-flash"

    def summarize(self, ticket: str) -> dict:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": INSTRUCCIONES},
                {"role": "user", "content": ticket},
            ],
            stream=True
        )
        texto = response.choices[0].message.content
        return json.loads(texto)
