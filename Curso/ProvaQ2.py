class Veiculo:
    def __init__(self,placa,valor,rodas,velocidade):
        self.placa = placa
        self.valor = valor
        self.quantidade_rodas = rodas
        self.velocidade = velocidade

    def __str__(self):
        return f'{self.placa},{self.valor},{self.quantidade_rodas},{self.velocidade}'



    def Acelerar(self):
        print(f'você está a {self.velocidade} km/h, e acelera.')


    def Frear(self):
        print(f'Você freiou!')


#Instância
v1 = Veiculo('1253-BRT',100.000,4,300)
print(v1)

v1.Acelerar()
v1.Frear()