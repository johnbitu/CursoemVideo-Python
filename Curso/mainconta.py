from cliente import Cliente
from Conta import Conta

nome = str(input("Nome do titular: "))
cpf = str(input("CPF do titular: "))
nasc = int(input("Data de nascimento do titular: "))
numero = str(input("Digite o Numero da conta: "))
saldo = float(input("Digite o seu saldo inicial: "))

pessoa1 = Cliente(nome,cpf,nasc)
conta1 = Conta(pessoa1,numero,saldo,100)

print("====================\n"+str(pessoa1),"\n"+"N°Conta:",conta1.numero_conta,"\n"+"Saldo: R${:.2f}".format(conta1.saldo),"\n====================")

resposta = ''
lista_resposta = ['DEPOSITAR','SACAR','CONSULTAR SALDO','SAIR']

while (resposta != 'SAIR'):
    resposta = str(input("\nVocê quer *depositar, *sacar, *consultar saldo ou *Sair: ")).upper()

    if(resposta == 'DEPOSITAR'):
        valor = float(input("\nDIGITE O VALOR DO DEPOSITO: "))
        conta1.depositar(valor)

    elif(resposta == 'SACAR'):
        valor =  float(input("\nDIGITE O VALOR DO SAQUE: "))
        conta1.sacar(valor)
    
    elif(resposta == 'CONSULTAR SALDO'):
        print("\n--- SEU SALDO É DE R${:.2f}" .format(conta1.saldo))

    elif(resposta not in lista_resposta):
        print("\nTente novamente . . .")