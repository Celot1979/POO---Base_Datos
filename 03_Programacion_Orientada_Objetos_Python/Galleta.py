    def __init__(self,sabor,forma,chocolate):
        self.sabor= sabor
        self.forma=forma
        self.chocolate = chocolate
    def hornear(self):
        print("La galleta de " +  self.sabor + " se está horneando... ¡Huele bien!")

    def __str__(self):
        tiene_chocolate = "con chocolate" if self.chocolate else "sin chocolate"
        return f"Soy una galleta {self.forma} de {self.sabor} {tiene_chocolate}"


primera_galleta = Galleta("fresa","cuadrada",False)
print(primera_galleta)
primera_galleta.hornear()

segunda_galleta= Galleta("platano", "redonda",True)
print(segunda_galleta)
segunda_galleta.hornear()