import random
pc = random.randint(0,10)

print('=_=' * 20)
print('Escolha qualquer numero de 0 a 10, e tente adivinhar qual numero eu pensei!')
print('=_=' * 20)

jogador = int(input('Em que numero eu pensei?'))

if jogador == pc:
    print('Você acertouuuu!')
else:
    print('Errouuuuuuuu!')

print(f'O número que você escolheu foi {jogador},e eu pensei no número {pc}!')