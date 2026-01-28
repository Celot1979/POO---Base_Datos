class Estudiante:
    def __init__(self, nombre: str, edad: int, nota_media: float):
        self.nombre = nombre
        self.edad = edad
        self.nota_media = nota_media

    def es_aprobado(self) -> bool:
        if self.nota_media >= 5.0:
            print("APROBADO")
            return True
        else:
            print("Suspenso")
            return False
        
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

Ana = Estudiante("Ana", 15, 8.5)
Ana.presentarse()
Ana.es_aprobado()

Luis = Estudiante("Luis", 15, 4.2)
Luis.presentarse()
Luis.es_aprobado()