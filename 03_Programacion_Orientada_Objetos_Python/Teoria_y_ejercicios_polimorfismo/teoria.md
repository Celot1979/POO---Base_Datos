# 🐍 Píldora Teórica: Polimorfismo en Python (UF2404)

> **Fecha Objetivo Examen:** 03/02/2026  
> **Bloque:** Programación Orientada a Objetos (MF0227_3)

## 1. ¿Qué es el Polimorfismo?
La palabra viene del griego "muchas formas". En programación, permite que objetos de diferentes clases respondan a la misma llamada de método (mensaje), pero cada uno implementando su propia lógica.

En Python, el polimorfismo es natural gracias al **Duck Typing** ("Si camina como un pato y hace cuac como un pato, entonces es un pato"). No necesitamos heredar obligatoriamente de una interfaz estricta (como en Java) para lograr esto, aunque la herencia ayuda a organizar el código.

## 2. Tipos comunes
### A. Sobreescritura de Métodos (Overriding)
Una clase hija modifica el comportamiento de un método heredado de la clase padre.

```python
class Animal:
    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"
```

### B. Polimorfismo con Funciones
Podemos crear funciones que acepten cualquier objeto, siempre que tenga el método esperado.

```python
def hacer_sonar(animal):
    print(animal.hablar())

# Funciona con Perro y Gato indistintamente
mi_perro = Perro()
mi_gato = Gato()

hacer_sonar(mi_perro) # Guau!
hacer_sonar(mi_gato)  # Miau!
```

## 3. ¿Por qué es importante para el Examen?
En la prueba práctica del 03/02/2026, es muy probable que te pidan diseñar un sistema donde diferentes entidades (ej: Usuarios, Empleados, Administradores) realicen una acción común (ej: `login()`) pero con comportamientos distintos.

> **Tip de Examen:** Si te piden "flexibilidad" o "extensibilidad", piensa en Polimorfismo. Permite agregar nuevas clases (ej: `Vaca`) sin cambiar la función `hacer_sonar`.

## 4. Documentación y Requisitos
Recuerda que para el examen debes tener tu DNI vigente y el DARDE actualizado si estás en situación de desempleo. ¡Revisa esto hoy mismo!
