import datetime
# dia = int(input('Qual o dia que você nasceu?'))
# mês = int(input('Qual o mês?'))
# ano = int(input('Qual o ano?'))

# d1 = datetime.date(ano,mês,dia)
data_entry = input('Coloque sua data de nascimento no formato YYYY/MM/DD:')
year, month, day = map(int, data_entry.split('/'))
d1 = datetime.date(year, month, day)

print(d1)