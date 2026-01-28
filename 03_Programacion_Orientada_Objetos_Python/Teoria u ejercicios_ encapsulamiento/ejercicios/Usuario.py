class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self,edad):
        if edad >=18 and edad <= 100:
            self._edad=edad
        else:
            print("Edad no valida") 

usuario = Usuario("Juan", 25)
print(usuario.edad)
usuario.edad = 12
print(usuario.edad)
usuario.edad = 45
print(usuario.edad)