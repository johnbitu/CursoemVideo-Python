from datetime import date

data = int(input('Qual o ano que você nasceu?'))
age = date.today().year - data

a1 = age - 18
a2 = 18 - age

if age < 18:
    print(f'Ainda vai servir!,mas fique esperto pois falta {a2} ano(s)')
elif age > 18:
    print(f'Já passou da hora de se alistar vagabundo!,agora como tu ficou sem se alistar por {a1} ano(s)?!')
else:
    print('Já está na hora de se alistar!')
