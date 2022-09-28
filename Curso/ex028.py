import random
pc = random.randint(0,5)

print('Escolha um numero de 1 a 5, e tente adivinhar qual o escolhido!')

jogador = int(input('Em que numero eu pensei?'))

print(f'O número escolhido foi {pc}')

if jogador == pc:
    print('você acertou!')
else:
    print('você errou!')