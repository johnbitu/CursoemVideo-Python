class Cliente():
    def __init__(self,nome,cpf,nasc):
        self.nome = nome
        self.cpf = cpf
        self.nasc = nasc
    
    def __str__(self):
        return("Nome: "+self.nome+" \nCPF: "+self.cpf +"\nNasc: "+ str(self.nasc))