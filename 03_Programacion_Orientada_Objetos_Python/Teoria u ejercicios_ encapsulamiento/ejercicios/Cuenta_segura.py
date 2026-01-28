class CuentaSegura:
    def __init__(self):
        self.__saldo = 2000
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        print("Error: No puedes manipular el saldo manualmente, usa depositar()")
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Error: La cantidad debe ser mayor a 0")
    def retirar(self, cantidad):
        if cantidad > 0 and self.__saldo >= cantidad:
            self.__saldo -= cantidad
        else:
            print("Error: La cantidad debe ser mayor a 0 y el saldo debe ser mayor o igual a la cantidad")


cuenta = CuentaSegura()
print(cuenta.saldo)
cuenta.depositar(500)
print(cuenta.saldo)
cuenta.retirar(200)
print(cuenta.saldo)
cuenta.saldo = 1000