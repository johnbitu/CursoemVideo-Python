nome = input('qual o seu nome?')
p = float(input('confirme o valor do seu salario:'))
p1 = p +(p * 15/100)
print('parabéns {},você acaba de receber um aumento pelo seus esforços'.format(nome))
print(f'seu salario atual é de {p1}')