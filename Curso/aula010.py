# tempo = int(input('Quantos anos tem seu carro?'))
# if tempo <=3:
#    print('Carro novo')
# else:
#    print('Carro velho')
# print('--FIM--')

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
média = (n1 + n2)/2
print(f'Sua média foi de {média :.1f}!')
if média >=6.0:
    print('Sua média foi boa, continue assim!')
else:
    print('Sua média foi baixa, precisa melhorar!')