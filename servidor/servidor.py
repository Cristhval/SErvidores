import os
import time
import hashlib

# Rutas a la carpeta compartida
RUTA_BASE = os.path.join(os.path.dirname(__file__), "..", "comunicacion")
ARCHIVO_ENTRADA = os.path.join(RUTA_BASE, "entrada_servidor.txt")
ARCHIVO_SALIDA = os.path.join(RUTA_BASE, "salida_servidor.txt")

INTERVALO_REVISION = 2  # segundos entre cada revisión



    # Procesa el mensaje: lo convierte a MAYÚSCULAS y lo invierte.
def procesar_mensaje(mensaje: str) -> str:
    return mensaje.upper()[::-1]


def leer_archivo(ruta: str) -> str:
    """Lee el contenido de un archivo de forma segura."""
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def escribir_archivo(ruta: str, contenido: str) -> None:
    """Escribe contenido en un archivo."""
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)


def main():
    print("=" * 55)
    print("  SERVIDOR DE MENSAJES INICIADO")
    print("=" * 55)
    print(f"  Vigilando: {ARCHIVO_ENTRADA}")
    print(f"  Escribiendo en: {ARCHIVO_SALIDA}")
    print(f"  Revisando cada {INTERVALO_REVISION} segundos...")
    print("  Presiona Ctrl+C para detener.\n")

    ultimo_hash = None


    contenido_inicial = leer_archivo(ARCHIVO_ENTRADA)
    if contenido_inicial:
        ultimo_hash = hashlib.md5(contenido_inicial.encode()).hexdigest()

    try:
        while True:
            contenido = leer_archivo(ARCHIVO_ENTRADA)

            # Manejar archivo vacío
            if not contenido:
                time.sleep(INTERVALO_REVISION)
                continue

            # Calcular hash del contenido actual
            hash_actual = hashlib.md5(contenido.encode()).hexdigest()

            # Solo procesar si es un mensaje nuevo
            if hash_actual != ultimo_hash:
                print(f"[NUEVO] Mensaje recibido: {contenido}")
                resultado = procesar_mensaje(contenido)
                escribir_archivo(ARCHIVO_SALIDA, resultado)
                print(f"[OK] Resultado escrito: {resultado}\n")

                ultimo_hash = hash_actual

            time.sleep(INTERVALO_REVISION)

    except KeyboardInterrupt:
        print("\n[!] Servidor detenido por el usuario.")


if __name__ == "__main__":
    main()