class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        print(f"Vehículo: {self.marca} {self.modelo}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, caballos: int):
         super().__init__(marca, modelo)
         self.caballos = caballos

    def descripcion(self):
        print(f"Coche: {self.marca} {self.modelo}, {self.caballos} CV")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, es_deportiva: bool):
        super().__init__(marca, modelo)
        self.es_deportiva = es_deportiva

    def caballito(self):
        if self.es_deportiva:
            print("¡Haciendo un caballito!")
        else:
            print("Mejor no arriesgarse")


# Zona de pruebas
v1 = Vehiculo("Seat", "Ibiza")
v1.descripcion()

c1 = Coche("Seat", "Ibiza", 150)
c1.descripcion()

m1 = Moto("Aprilia", "Classic", True)
m1.caballito()