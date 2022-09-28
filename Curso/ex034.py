sal = float(input('Qual o valo do seu salario?'))
v1 = sal * 0.10
v2 = sal * 0.15

r1 = v1 + sal
r2 = v2 + sal
if sal>=1250:
    print(f'O valor do seu salario de {sal:.2f}, teve um aumento para {r1:.2f}')
else:
    print(f'O seu salario teve um aumento de {sal:.2f}, para {r2:.2f}')
