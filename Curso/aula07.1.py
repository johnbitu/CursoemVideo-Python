n1 = int(input('digite um numero:'))
n2 = int(input('digite outro:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r1 = n1 ** (1/2)
r2 = n2 ** (1/2)
print('o valor da multiplicação é \033[4;37m{}\033[m,\n da soma \033[4;36m{}\033[m,\n da divisão \033[4;35m{}\033[m,'.format(m,s,d),end=' = ')
print('da divisão inteira \033[4;34m{}\033[m,\n da exponenciação \033[4;33m{}\033[m,\n da raiz de \033[4;32m{}\033[m é {:.3},\n e a raiz de {} é \033[4;31m{}\033[m '.format(di,e,n1,r1,n2,r2))