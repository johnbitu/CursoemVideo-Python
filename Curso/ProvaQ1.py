class Casa:
    def __init__(self, quarto, bathroom, local, aluguel ):
        self.quarto = quarto
        self.bathroom = bathroom
        self.local = local
        self.aluguel = aluguel

    def __str__(self):
        Casa(f'{self.quarto},{self.bathroom},{self.local},{self.aluguel}')
        return

    def caract(self):
        print(f'{self.quarto} quarto(s),{self.bathroom} banheiro(s),{self.local},{self.aluguel}')
        return

    def alugar_casa(self):
        print('casa alugada')
        return

    def devolver_casa(self):
        print('casa disponivel')
        return


c1 = Casa('2', '3', 'Rua_Andorinha', '1300R$')

c1.caract()
c1.alugar_casa()
c1.devolver_casa()