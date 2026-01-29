"""
MONITOR DEL SISTEMA (Agente de Sistemas)
-----------------------------------------
Objetivo: Usar Python para obtener información de tu Mac.
Nivel: Principiante en Sistemas / Intermedio en Python.

PASO 1: Identificación
Vamos a usar una librería que ya viene con Python llamada 'platform'.
No necesitas instalar nada.

Documentación rápida:
- platform.system() -> Te dice el SO (ej: 'Darwin' para Mac, 'Windows').
- platform.release() -> La versión del kernel.
- platform.processor() -> El "cerebro" (Intel/M1/M2).
"""

# 1. IMPORTAR LIBRERÍAS
# (Tu código aquí: importa la librería 'platform')


def mostrar_informacion_basica():
    print("--- INFORMACIÓN DEL SISTEMA ---")
    
    # 2. OBTENER DATOS
    # Crea variables para guardar:
    # - El sistema operativo (sistema)
    # - La versión (version_so)
    # - El procesador (cerebro)
    
    # (Tu código aquí)


    # 3. MOSTRAR DATOS
    # Usa print con f-strings (f"...") para mostrarlo bonito.
    
    # (Tu código aquí)

# Bloque principal
if __name__ == "__main__":
    mostrar_informacion_basica()
