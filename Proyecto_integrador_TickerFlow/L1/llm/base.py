"""
El CONTRATO: define qué debe saber hacer todo proveedor de IA.

No hace nada por sí solo. Solo dice: "todo proveedor tiene un método
summarize que recibe un ticket (texto) y devuelve un dict".
"""

# Instrucciones (prompt de sistema) que comparten todos los proveedores.
# Le pedimos JSON para poder convertir la respuesta en un dict.
INSTRUCCIONES = (
    "Resume el ticket de soporte que te pasa el usuario. "
    "Responde SOLO con un JSON válido, sin texto extra, con estas claves: "
    '"resumen" (texto corto) y "prioridad" ("baja", "media" o "alta").'
)


class Provider:
    def summarize(self, ticket: str) -> dict:
        # Si una clase hija olvida implementar este método, falla con un mensaje claro.
        raise NotImplementedError("Cada proveedor debe implementar summarize()")
