# La "recepción" del paquete: permite escribir `from llm import Router`
# en lugar de `from llm.router import Router`.
from llm.base import Provider
from llm.gemini_provider import GeminiProvider
from llm.groq_provider import GroqProvider
from llm.router import Router

# Lo que este paquete ofrece públicamente.
__all__ = ["Provider", "GroqProvider", "GeminiProvider", "Router"]
