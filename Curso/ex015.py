dias = int(input('quantos dias alugados?'))
km = float(input('quantos Km rodados?'))
p = dias * 60
k = km * 0.15
t = p + k
print('o valor a pagar é de {:.2f}'.format(t))