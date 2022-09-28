import datetime
from datetime import date

ano = int(input('Em que ano você nasceu?'))
# Idade
age = date.today().year - ano

print(f'Você tem {age} anos e foi categorizado como:')

# Condição
if age<=9:
    print('Categoria \033[4;36mMirim!\033[m')
elif age<=14:
    print('Categoria \033[4;34mInfantil!\033[m')
elif age<=19:
    print('Categoria \033[4;35mJunior!\033[m')
elif age<=20:
    print('Categoria \033[4;32mSenior!\033[m')
elif age>20:
    print('Categoria \033[4;31mMaster!\033[m')