n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

if n1>n2:
    print('O primeiro número é \033[1;32;107mmaior\033[m')
elif n1<n2:
    print('O segundo número é \033[1;32;107mmaior\033[m')
else:
    print('Os números são \033[1;32;107miguais\033[m')
