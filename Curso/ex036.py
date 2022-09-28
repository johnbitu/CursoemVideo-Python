casa = float(input('Qual o valor da casa?'))
sal = float(input('Qual o valor do seu salário?'))
anos = int(input('Em quantos anos conseguirá pagar?'))

p1 = anos * 12
p2 = casa/p1

s1 = sal * 0.30

print(f'O valor da prestação é {p2}')
print(f'O valor que não poderá exeder é de {s1}')
if p2<=s1:
    print(f'Parabens, sua compra foi aprovada e pagará \033[1;30;107m{p2:.1f}\033[m de prestação mensal.')
else:
    print('A prestação execedeu 30% do seu salário, sua compra foi \033[1;31;40mnegada\033[m!')