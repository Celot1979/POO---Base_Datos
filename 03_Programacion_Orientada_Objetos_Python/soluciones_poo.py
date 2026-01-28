# Soluciones POO Básica - IFCD0112 / Curso Gijón

# --- EJERCICIO 1: GALLETA ---
print("--- EJERCICIO 1 ---")

class Galleta:
    def __init__(self, sabor, forma, tiene_chocolate):
        self.sabor = sabor
        self.forma = forma
        self.tiene_chocolate = tiene_chocolate
    
    def hornear(self):
        print(f"La galleta de {self.sabor} con forma de {self.forma} se está horneando... ¡Huele bien!")

# Pruebas
galleta1 = Galleta("Vainilla", "Estrella", False)
galleta2 = Galleta("Jengibre", "Hombrecito", True)

galleta1.hornear()
galleta2.hornear()
print("\n")


# --- EJERCICIO 2: ESTUDIANTE ---
print("--- EJERCICIO 2 ---")

class Estudiante:
    def __init__(self, nombre, edad, nota_media):
        self.nombre = nombre
        self.edad = edad
        self.nota_media = nota_media
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
        
    def es_aprobado(self):
        return self.nota_media >= 5.0

# Pruebas
ana = Estudiante("Ana", 25, 8.5)
luis = Estudiante("Luis", 22, 4.2)

ana.presentarse()
print(f"¿Ana aprobó?: {ana.es_aprobado()}")

luis.presentarse()
print(f"¿Luis aprobó?: {luis.es_aprobado()}")
print("\n")


# --- EJERCICIO 3: CUENTA BANCARIA ---
print("--- EJERCICIO 3 ---")

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depositados {cantidad}€. Nuevo saldo: {self.saldo}€")
        else:
            print("La cantidad a depositar debe ser positiva.")
            
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print(f"Fondos insuficientes. Tienes {self.saldo}€ e intentas sacar {cantidad}€.")
        else:
            self.saldo -= cantidad
            print(f"Retirados {cantidad}€. Nuevo saldo: {self.saldo}€")
            
    def ver_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo}€")

# Pruebas
mi_cuenta = CuentaBancaria("Daniel", 100)
mi_cuenta.ver_saldo()
mi_cuenta.depositar(50)
mi_cuenta.retirar(200) # Fallo intencionado
mi_cuenta.retirar(20)  # Éxito
