# Unidad Formativa: POO Refuerzo - Encapsulamiento
## Bloque: Calidad de Código y Seguridad

### 1. ¿Por qué Encapsular?
Hasta ahora, cualquiera podía cambiar los datos de nuestros objetos libremente:
```python
coche.caballos = -500  # ¡Esto no tiene sentido pero Python lo permitía!
```
El encapsulamiento protege los datos para evitar valores inválidos o incoherentes.

### 2. Atributos "Privados"
En Python, ponemos dos guiones bajos `__` delante del nombre del atributo para indicar que **no se debe tocar desde fuera**.

```python
class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # Privado
```
Si intentas acceder a `c.__saldo` te dará error.

---

### 3. La forma Pythonica: Propiedades (`@property`)
En lugar de crear métodos gigantes como `get_saldo()` o `set_saldo()`, Python usa **decoradores**. Esto permite usar el atributo como si fuera una variable normal, pero ejecutando código de validación por detrás.

```python
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad  # Un guion bajo: convención de "protegido"

    # GETTER: Para LEER
    @property
    def edad(self):
        return self._edad

    # SETTER: Para MODIFICAR (con validación)
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            print("¡La edad no puede ser negativa!")
        else:
            self._edad = nueva_edad

# USO
u = Usuario("Ana", 25)
u.edad = -5  # Salta el aviso: "¡La edad no puede ser negativa!"
print(u.edad) # Imprime 25 (el valor no cambió)
```
