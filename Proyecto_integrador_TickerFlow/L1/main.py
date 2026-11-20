from dotenv import load_dotenv

# Primero cargamos el .env, ANTES de crear los proveedores,
# porque ellos leen las claves de os.environ.
load_dotenv()

from llm import Router  # noqa: E402  (import después de load_dotenv a propósito)


def main():
    router = Router(primary="groq", fallback="gemini")

    ticket = "Queria saber si tiene descuentas en almacenes"
    resultado = router.summarize_ticket(ticket)

    # resultado es un dict, así que accedemos a sus valores por clave.
    print("Resumen:  ", resultado["resumen"])
    print("Prioridad:", resultado["prioridad"])


if __name__ == "__main__":
    main()
