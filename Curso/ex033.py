n1 = float(input('Digite um número:'))
n2 = float(input('Digite um número:'))
n3 = float(input('Digite um número:'))

menor = n1
maior = n2
#O número menor!
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
#O número maior!
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print(f'O menor número é {menor}!')
print(f'O maior número é {maior}!')