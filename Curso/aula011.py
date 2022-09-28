# print('\033[1;36;41mOlá Mundo\033[m')


# nome = input('Qual o seu nome?')
# print(f'O seu nome é \033[36m{nome}\033[m!!!!')

# criar uma 'biblioteca de cores'
cores = {'limpa':'\033[m',
         'azul claro':'\033[36m',
         'roxosub':'\033[4;35m',
         'pretoebranco':'\033[7m'}
nome = 'John'
print('Seja bem vindo {}{}{}'.format(cores['pretoebranco'],nome,cores['limpa']))