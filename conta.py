

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.get_saldo(), self.get_titular()))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)  # Objeto conta origem
        destino.saca(valor)  # Objeto conta destino

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite

    def set_titular(self, titular):
        self.__titular = titular

    def set_saldo(self, saldo):
        self.__saldo = saldo
