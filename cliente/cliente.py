import os
import time

# Rutas a la carpeta compartida
RUTA_BASE = os.path.join(os.path.dirname(__file__), "..", "comunicacion")
ARCHIVO_ENTRADA = os.path.join(RUTA_BASE, "entrada_servidor.txt")
ARCHIVO_SALIDA = os.path.join(RUTA_BASE, "salida_servidor.txt")

TIEMPO_ESPERA = 3  # segundos simulando latencia


def escribir_archivo(ruta: str, contenido: str) -> None:
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)


def leer_archivo(ruta: str) -> str:
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return ""


def enviar_mensaje(mensaje: str) -> str:
    """
    Envía un mensaje al servidor (escribiéndolo en el archivo de entrada)
    y espera la respuesta (leyendo el archivo de salida).
    """
    # 1. Escribir en el archivo de entrada
    escribir_archivo(ARCHIVO_ENTRADA, mensaje)
    print(f"   Mensaje enviado: '{mensaje}'")

    # 2. Esperar la latencia (simulada)
    print(f"   Esperando respuesta ({TIEMPO_ESPERA}s)...")
    time.sleep(TIEMPO_ESPERA)

    # 3. Leer la respuesta
    respuesta = leer_archivo(ARCHIVO_SALIDA)
    return respuesta


def main():
    print("=" * 55)
    print("  CLIENTE DE MENSAJES")
    print("=" * 55)
    print("  Escribe 'salir' para terminar.\n")

    while True:
        mensaje = input("Ingresa un mensaje: ").strip()

        if not mensaje:
            print("    El mensaje no puede estar vacío.\n")
            continue

        if mensaje.lower() == "salir":
            print("   Cerrando cliente...")
            break

        respuesta = enviar_mensaje(mensaje)

        if respuesta:
            print(f"   Respuesta del servidor: {respuesta}\n")
        else:
            print("    No se recibió respuesta. ¿Está el servidor ejecutándose?\n")


if __name__ == "__main__":
    main()