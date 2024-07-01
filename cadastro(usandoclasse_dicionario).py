i = 0 #nao pode ter mais de 15 contas e nao pode repetir

class clientes:
    def __init__(self,conta, nome, saldo):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo
        print(self.conta,self.nome,self.saldo)
    def cliente(self):
        print(self.conta,self.nome,self.saldo) #essa segunda aparentemente nao roda

Mariana = clientes('110','Mariana','30')
Vitor = clientes('110','Vitor','30')

