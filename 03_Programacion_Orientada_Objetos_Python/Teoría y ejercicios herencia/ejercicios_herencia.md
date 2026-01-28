# Desafío Práctico: Herencia y Polimorfismo
## Certificado IFCD0112

### Ejercicio 1: Concesionario de Vehículos ✅
Crea una jerarquía de clases para un concesionario.
1.  **Clase Padre `Vehiculo`**:
    *   Constructor: marca (str), modelo (str).
    *   Método `descripcion()`: imprime "Vehículo: [marca] [modelo]".
2.  **Clase Hija `Coche`** (hereda de Vehiculo):
    *   Constructor: incluye `caballos` (int). Usa `super()`.
    *   Método `descripcion()`: Sobreescríbelo para añadir los caballos: "Coche: [marca] [modelo], [caballos] CV".
3.  **Clase Hija `Moto`** (hereda de Vehiculo):
    *   Constructor: incluye `es_deportiva` (bool).
    *   Método `caballito()`: Si es deportiva imprime "¡Haciendo un caballito!", si no "Mejor no arriesgarse".

**Prueba:** Crea un coche y una moto e invoca sus métodos.

---

### Ejercicio 2 (Reto): f (Polimorfismo)
1.  Crea una clase padre `Figura` con un método `area()` que no haga nada o retorne 0.
2.  Crea la clase `Rectangulo`:
    *   Constructor: `base` (float), `altura` (float).
    *   Método `area()`: Retorna base * altura.
3.  Crea la clase `Circulo`:
    *   Constructor: `radio` (float).
    *   Método `area()`: Retorna 3.14 * radio * radio.
4.  **Prueba Polimórfica**:
    *   Crea una lista con un rectángulo y un círculo.
    *   Recorre la lista con un bucle `for` y llama a `.area()` de cada uno. ¡Verás que cada uno calcula su área correctamente!
