i = 0 #nao pode ter mais de 15 contas e nao pode repetir

class clientes:
    def __init__(self,conta, nome, saldo):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo
        print(self.conta,self.nome,self.saldo)
    def cliente(self):
        print(self.conta,self.nome,self.saldo) 
        print('escada')#essa segunda aparentemente nao roda

while i <= 15:
    nome = input('qual seu nome?')
    saldo = input('quanto voce tem na conta?')
    clientes(i,nome,saldo)
    i += 1
print('fim')
clientes()
