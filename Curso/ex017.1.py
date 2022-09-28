import math
co = int(input('o comprimento do cateto oposto:'))
ca = int(input('o comprimento do cateto adjacente:'))
hi = math.hypot(co,ca)
print('o comprimento da hipotenusa é {:.3f}!'.format(hi))