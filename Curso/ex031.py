print('-==-'* 5)
print('SEJA BEM VINDO\n BITUTURISMOS')
print('-==-'* 5)

viagem = float(input('Qual a distância da viagem?'))

v1 = viagem * 0.50
v2 = viagem * 0.45
if viagem<=200:
    print(f'O valor da viagem ficou no total de {v1} reais!')
else:
    print(f'Já que a distância passou de 200km, vai pagar menos, o valor no total é {v2} reais!')