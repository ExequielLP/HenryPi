"""
REINTENTOS que respetan la señal del proveedor (Retry-After).

Si el proveedor dice cuánto esperar, le hacemos caso.
Si no dice nada, calculamos nosotros con backoff exponencial + jitter.
"""

import random
import time

from openai import RateLimitError


def call_with_backoff(fn, max_retries=5):
    for intento in range(max_retries):
        try:
            return fn()
        except RateLimitError as e:
            if intento == max_retries - 1:
                raise  # se acabaron los intentos: el router pasa al plan B

            # 1) ¿El proveedor nos dice cuánto esperar? Le hacemos caso.
            retry_after = e.response.headers.get("retry-after")
            if retry_after:
                espera = float(retry_after)
            # 2) Si no dice nada, calculamos nosotros (backoff exponencial + jitter).
            else:
                espera = (2 ** intento) + random.uniform(0, 1)

            print(f"[retry] intento {intento + 1} falló, esperando {espera:.1f}s...")
            time.sleep(espera)
