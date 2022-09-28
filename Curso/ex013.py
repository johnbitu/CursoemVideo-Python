nome = input('qual o seu nome?')
p = float(input('confirme o valor do seu salario:'))
p1 = p * 0.15
p2 = p + p1
print('parabéns {},você acaba de receber um aumento pelo seus esforços'.format(nome))
print('seu salario atual é de {}'.format(p2))