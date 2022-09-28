n1 = float(input('Qual a sua nota parcial?'))
n2 = float(input('Qual a sua nota bimestral?'))

# Média
m1 = (n1+n2)/2
print(f'Você tirou {m1}!')

# Condição
if m1 <= 5:
    print('Porra mlk, muito burro filho,\033[1;31;40mReprovadoooo!!!!\033[m')
elif m1 <= 6.9:
    print('Hmm quase meu mano,mas você tem uma segunda chance,\033[1;34;40mRecuperação!\033[m')
elif m1 >= 7:
    print('Boa krl,tu conseguiu passar na média,\033[1;32;40mAprovadoo!!!!\033[m')