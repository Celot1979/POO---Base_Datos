class Figura:
    def area(self):
        return 0

class Rectangulo(Figura):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * self.radio * self.radio


# Prueba Polimórfica
# 1. Creamos la lista con objetos variados
mis_figuras = [
    Rectangulo(2.0, 3.0),
    Circulo(22),
    Rectangulo(10.0, 10.0)
]

print("\n--- Inicio del bucle polimórfico ---")
# 2. Recorremos la lista. No nos importa si es Rectangulo o Circulo, solo que tenga .area()
for figura in mis_figuras:
    print(f"Soy una figura y mi área es: {figura.area()}")