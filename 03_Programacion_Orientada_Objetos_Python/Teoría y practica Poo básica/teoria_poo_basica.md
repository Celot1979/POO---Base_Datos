# Lección 3: Introducción a la Programación Orientada a Objetos (POO) en Python
## Certificado IFCD0112 - Preparación Examen (03/02/2026)

La Programación Orientada a Objetos (POO) es un modelo de programación que organiza el diseño de software alrededor de **datos** (objetos) en lugar de funciones y lógica.

### 1. Conceptos Clave: Clase vs Objeto

Imagina que eres un arquitecto de coches.

*   **Clase (Class):** Es el **plano** o molde. Define cómo serán los coches (tienen 4 ruedas, motor, color, etc.), pero no es un coche real que puedas conducir.
*   **Objeto (Object/Instance):** Es el **coche fabricado** siguiendo ese plano. Puedes tener el "Coche Rojo de Juan" y el "Coche Azul de María". Ambos vienen de la misma clase `Coche`, pero son objetos distintos.

### 2. Sintaxis en Python

#### Definir una Clase
Usamos la palabra clave `class`. Por convención, los nombres de clases usan `CamelCase` (Mayúscula inicial).

```python
class Coche:
    pass  # 'pass' indica que está vacío por ahora
```

#### El Constructor (`__init__`)
Es un método especial que se ejecuta automáticamente al crear un objeto. Sirve para inicializar los **atributos** (características).

*   `self`: Es una referencia a *este* objeto específico que se está creando. **Siempre** es el primer parámetro.

```python
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca      # Atributo: marca
        self.modelo = modelo    # Atributo: modelo
        self.color = color      # Atributo: color
```

#### Métodos (Comportamiento)
Son funciones dentro de la clase que definen qué puede **hacer** el objeto.

```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def arrancar(self):
        self.encendido = True
        print(f"El {self.marca} {self.modelo} ha arrancado.")

    def tocar_claxon(self):
        print("¡Mec mec!")
```

### 3. Creando Objetos (Instanciación)

```python
# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")

# Usar sus atributos
print(mi_coche.marca)  # Salida: Toyota

# Usar sus métodos
mi_coche.arrancar()    # Salida: El Toyota Corolla ha arrancado.
mi_coche.tocar_claxon() # Salida: ¡Mec mec!
```

### Resumen para el Examen
*   **Clase**: Definición/Plantilla.
*   **Objeto**: Instancia concreta.
*   **`__init__`**: Método constructor para estado inicial.
*   **`self`**: Referencia a la propia instancia.
