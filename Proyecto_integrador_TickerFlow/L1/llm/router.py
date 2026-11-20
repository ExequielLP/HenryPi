"""
ROUTER: decide qué proveedor usar y tiene un plan B (fallback).

El resto del programa solo llama a router.summarize_ticket(ticket)
y no necesita saber qué modelo respondió.
"""

from openai import RateLimitError

from llm.gemini_provider import GeminiProvider
from llm.groq_provider import GroqProvider
from llm.retry import call_with_backoff


class Router:
    def __init__(self, primary: str = "groq", fallback: str = "gemini"):
        # Diccionario: nombre del proveedor -> objeto adaptador.
        self.adapters = {
            "groq": GroqProvider(),
            "gemini": GeminiProvider(),
        }
        self.primary = primary
        self.fallback = fallback

    def summarize_ticket(self, ticket: str) -> dict:
        try:
            # Plan A: el proveedor principal, con reintentos.
            # lambda: le pasamos "la receta" para que call_with_backoff la ejecute cuando quiera.
            return call_with_backoff(lambda: self.adapters[self.primary].summarize(ticket))
        except RateLimitError:
            # Plan B: si tras todos los reintentos sigue sin cuota (error 429), usamos el respaldo.
            print(f"[router] {self.primary} sin cuota tras reintentar, usando {self.fallback}...")
            return self.adapters[self.fallback].summarize(ticket)
