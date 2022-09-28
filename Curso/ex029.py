km = float(input('A que velocidade você está?'))

print(f'Sua velocidade é de {km :.2f}km/h')
if km<=80:
    print('Sua velocidade está dentro da velocidade permitida!')
else:
    print('Você excedeu a velocidade permitida e será multado!')
    multa = (km-80) * 7
    print(f'O valor da multa será de {multa:.3f} reais')