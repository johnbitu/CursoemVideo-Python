frase = 'Curso em Video Python'
# Exemplos de Fatiamentos:
# Pega a letra onde está o número. [9]
# Pega o trecho onde foi demarcado. [9:13]
# Pega o trecho onde foi demarcado e pula de 2 em 2. [9:21:2]
# Começa onde foi marcado e termina anterior ao número. [:5]
# Começa onde foi marcado e termina sucessor ao número. [15:]
# Começa onde foi marcado e pula de 3 em 3. [9::3]

# Exemplos de Análise:
# Contagem de caracteres totais em frase usa "len()". len(frase)
# Contagem de caracteres especificos em frase usa ".count('')". frase.count('o')
# Contagem já com fatiamento. frase.count('o',0,14)
# Função para achar certa parte ou trecho de uma palavra. Receber -1 significa que n existe esse valor. frase.find('deo')
# Ele irá falar se existe a tal palavra ou frase. 'curso' in frase

# Exemplos de Transformação:
# Essa função irá substituir uma palavra pela outra. frase.replace('Python','Android')
# Essa função substitui o que está em minusculo por maiusculo. frase.upper()
# Essa função substitui o que está em maiusculo por minusculo. frase.lower()
# Essa função transformar tudo que está em maiusculo em minuscolo menos a primeira letra da Frase. frase.capitalize()
# Irá transformar todo começo da palavra em maiusculo. frase.title()
# Vai remover o espaço que começa e que termina a frase.  frase.strip() dependendo da direção colocar 'r' ou 'l'. frase.rstrip()
print(frase.count(''))
