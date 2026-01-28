class CuentaBancaria:
    def __init__(self, titular: str, saldo: int = 0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad: int):
        self.saldo += cantidad

    def retirar(self, cantidad: int):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def ver_saldo(self):
        print(f"El saldo actual de la cuenta bancaria es: {self.saldo}")


# Zona de pruebas
dani = CuentaBancaria("Daniel", 800)
dani.ver_saldo()

# Intento de retiro excesivo
dani.retirar(1200)
dani.ver_saldo()

# Depósito y retiro válido
dani.depositar(500)
dani.retirar(200)
dani.ver_saldo()
