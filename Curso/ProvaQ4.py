class Cliente:
    def __init__(self, nome, cpf, sexo, email, junior, pleno, senior):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.email = email
        self.cargos = [junior,pleno,senior]

    def __str__(self):
        return f'{self.nome},{self.cpf},{self.sexo},{self.email},{self.cargos}'



h2 = Cliente(f'John', '032.233.932-49', 'Masculino', 'johnvwer@gmail.com',)
print(h2)

h2.enviar_email()