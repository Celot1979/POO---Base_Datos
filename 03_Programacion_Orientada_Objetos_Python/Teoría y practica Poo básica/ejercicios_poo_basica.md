# Desafío Práctico: Fundamentos POO Python
## Certificado IFCD0112

Para aprobar este bloque, debes ser capaz de traducir entidades del mundo real a código Python usando clases.

### Ejercicio 1: El Molde de Galletas ✅
Crea una clase llamada `Galleta`.
1.  El constructor debe recibir `sabor` (str) y `forma` (str) y si tiene `chocolate` (bool).
2.  Crea un método `hornear()` que imprima: "La galleta de [sabor] se está horneando... ¡Huele bien!".
3.  Crea dos objetos (galletas) distintos e invoca sus métodos.


### Ejercicio 2: Sistema de Estudiantes ✅
Crea una clase llamada `Estudiante`.
1.  **Atributos**: `nombre` (str), `edad` (int), `nota_media` (float).
2.  **Método** `es_aprobado()`: Devuelve `True` si la `nota_media` es 5.0 o superior, y `False` si no.
3.  **Método** `presentarse()`: Imprime "Hola, soy [nombre] y tengo [edad] años".

**Prueba tu código:**
Crea un estudiante llamado "Ana" con nota 8.5 y otro "Luis" con nota 4.2. Comprueba si han aprobado imprimiendo el resultado del método `es_aprobado()`.

### Ejercicio 3 (Reto): La Cuenta Bancaria ✅
Crea una clase `CuentaBancaria`.
1.  **Atributos**: `titular` y `saldo` (inicialízalo en 0 si no se da otro valor).
2.  **Método** `depositar(cantidad)`: Suma la cantidad al saldo.
3.  **Método** `retirar(cantidad)`: Resta la cantidad si hay saldo suficiente. Si no, imprime "Fondos insuficientes".
4.  **Método** `ver_saldo()`: Imprime el saldo actual.
