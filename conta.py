

class Conta:
    def __init__(self):
        print("Construindo objeto...{}".format(self))
        self.__numero = 123
        self.__titular = "Nico"
        self.__saldo = 55.0
        self.__limite = 1000.0

def extrato(self):
    print('Saldo de {} do titular {}'.format(self.saldo, self.titular))

def deposita(self, valor):
    self.saldo += valor

def saca(self, valor):
    self.saldo -= valor

def transfere(self, valor, destino):
    self.saca(valor)  # Objeto conta origem
    destino.saca(valor)  # Objeto conta destino
