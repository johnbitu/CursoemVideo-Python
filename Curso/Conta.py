class Conta():
    def __init__(self, cliente, numero_conta,saldo,limite):
        self.cliente = cliente
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.limite = limite

    def sacar(self,valor):
        if(self.saldo+self.limite < valor):
            print("Não é possivel sacar esse valor!")
        else:
            self.saldo -= valor
            print("Foi sacado R${} da sua conta!".format(valor),"Saldo; R${:.2f}".format(self.saldo))

    def depositar(self,valor):
        if(valor <= 0):
            print("Não é possivel depositar esse valor!")
        else:
            self.saldo += valor
            print("Foi depositado R${} na sua conta!" .format(valor), "Saldo: R${:.2f}".format(self.saldo))