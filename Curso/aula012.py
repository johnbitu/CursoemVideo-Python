# condição aninhada
# if():


# pode por quantos elif quiser.
# elif():
# elif():

# só pode ter um ou nenhum else.
# else():

# Usar or ou in.

nome = input('Qual o seu nome?')

if nome == 'John':
    print('Que nome bonito!')
elif nome == 'Mario' or nome == 'Pedro' or nome == 'Guilherme':
    print('Que nome meio \033[1;31mSUSSSS!!!!\033[m')
else:
    print('Seu nome é normal.')
print(f'Tenha um bom dia,\033[4;36m{nome}\033[m!')