ano = int(input('Que ano você deseja saber se é bissexto?'))

if ano % 4 == 0:
    print(f'O ano de {ano} é Bissexto!')
else:
    print(f'O ano de {ano} não é Bissexto!')