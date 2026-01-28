# Unidad Formativa: Programación Orientada a Objetos (Avanzado)
## Bloque: Herencia y Polimorfismo

### 1. ¿Qué es la Herencia? (DRY - Don't Repeat Yourself)
La herencia nos permite crear nuevas clases basadas en clases existentes. Es como la genética: un hijo hereda características de sus padres, pero puede tener las suyas propias.

**Sintaxis:**
```python
class Animal:         # Clase PADRE (Superclase)
    def respirar(self):
        print("Respirando...")

class Perro(Animal):  # Clase HIJA (Subclase)
    def ladrar(self):
        print("Guau!")
```

En este ejemplo, `Perro` **es un** `Animal`. Tiene acceso al método `respirar()` aunque no esté escrito dentro de `Perro`.

---

### 2. La función `super()`
Se usa para llamar a métodos de la clase padre. Es muy común en el constructor `__init__` para aprovechar la inicialización del padre.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llama al constructor de Persona
        self.salario = salario        # Atributo exclusivo de Empleado
```

---

### 3. Polimorfismo y Sobreescritura (Overriding)
Las clases hijas pueden modificar el comportamiento de los métodos del padre.

```python
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):  # Sobreescribe el método
        return "Guau"

class Gato(Animal):
    def hablar(self):  # Sobreescribe el método
        return "Miau"
```

El polimorfismo permite tratar a `Perro` y `Gato` simplemente como `Animal`, y cada uno responderá a su manera.
