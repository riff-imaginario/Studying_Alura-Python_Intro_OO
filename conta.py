

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

def extrato(self):
    print('Saldo de {} do titular {}'.format(self.saldo, self.titular))

def deposita(self, valor):
    self.saldo += valor

def saca(self, valor):
    self.saldo -= valor

def transfere(self, valor, destino):
    self.saca(valor)  # Objeto conta origem
    destino.saca(valor)  # Objeto conta destino
