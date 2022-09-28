import random
from pygame import mixer

a1 = str(input('Primeiro suspeito:'))
a2 = str(input('Segundo suspeito:'))
a3 = str(input('Terceiro suspeito:'))
a4 = str(input('Quarto suspeito:'))
a5 = str(input('Quinto suspeito:'))
a6 = str(input('Sexto suspeito:'))

lista = [a1,a2,a3,a4,a5,a6]

escolhido = random.choice(lista)

print(f'Então o gay é o {escolhido}!')

# Musica dramatica

mixer.init()
mixer.music.load('X2Convert.cc - Gloria Gaynor - I Will Survive (Official Video) (128 kbps).mp3')
mixer.music.play()
input()