class Caderno:
    def __init__(self,paginas,cor):
        self.paginas = paginas
        self.cor = cor


    def __str__(self):
        return f'{self.paginas},{self.cor}'


    def passar_pagina(self):
        print('Você passou uma pagina!')
        return

    def voltar_pagina(self):
        print('Você voltou uma pagina!')
        return



p1 = Caderno('20 paginas','Branco')
print(p1)

p1.passar_pagina()
p1.voltar_pagina()