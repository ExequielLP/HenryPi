"""
ADAPTADOR para Groq: sabe cómo hablar con la API de Groq,
pero por fuera cumple el mismo contrato que cualquier Provider.
"""

import json
import os

from openai import OpenAI

from llm.base import INSTRUCCIONES, Provider


class GroqProvider(Provider):
    def __init__(self):
        # __init__ se ejecuta al crear el objeto: GroqProvider()
        # Aquí preparamos el cliente y elegimos el modelo.
        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ["GROQ_API_KEY"],
            max_retries=0,  # los reintentos los maneja nuestro llm/retry.py
        )
        self.model = "openai/gpt-oss-120b"

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
        # json.loads convierte el texto JSON en un dict de Python.
        return json.loads(texto)
