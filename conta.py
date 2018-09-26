

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construção de objeto em {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo da conta é R${}".format(self.saldo))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


