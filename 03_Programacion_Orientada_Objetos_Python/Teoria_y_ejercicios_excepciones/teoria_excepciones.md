# Píldora Teórica: Manejo de Excepciones y Errores

Hasta ahora, si tu programa fallaba (ej: dividir por 0), se detenía abruptamente y mostraba un error "rojo" en la consola. Eso es inaceptable en un programa profesional.

Python usa bloques `try...except` para manejar estas situaciones con elegancia.

## Estructura Básica

```python
try:
    # Código que PUEDE fallar
    numero = int(input("Dime un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")

except ValueError:
    # Se ejecuta si el usuario escribe letras en vez de números
    print("¡Error! Debes escribir un número válido.")

except ZeroDivisionError:
    # Se ejecuta si el usuario escribe 0
    print("¡Error! No se puede dividir entre cero.")

except Exception as e:
    # Se ejecuta para cualquier otro error no previsto
    print(f"Ha ocurrido un error inesperado: {e}")

else:
    # Se ejecuta SOLO si NO hubo ningún error en el try
    print("Todo salió perfecto.")

finally:
    # Se ejecuta SIEMPRE (haya error o no). Útil para cerrar archivos o bases de datos.
    print("Operación finalizada.")
```

---

## Ejercicio: La Calculadora Robusta

Vas a crear un script `Calculadora_segura.py` que sea imposible de romper.

### Requisitos:
1.  Crea una función `dividir_numeros()`.
    *   Pide al usuario dos números (`a` y `b`).
    *   Intenta dividirlos.
    *   **Maneja `ValueError`**: Si mete letras, dile "Introduce solo números".
    *   **Maneja `ZeroDivisionError`**: Si b es 0, dile "No dividas por cero".
    *   Usa un bucle `while True` para que, si falla, vuelva a preguntar hasta que lo haga bien.

2.  (Opcional) Crea una función `leer_archivo_config()`:
    *   Intenta abrir un archivo llamado `config.txt` (que no existe).
    *   Maneja el `FileNotFoundError` e imprime "Archivo de configuración no encontrado, usando valores por defecto".
