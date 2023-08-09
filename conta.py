class Conta:

    def __init__(self, numero, titular, saldo, limite): #função construtora
        print('Construindo um objeto...'.format(self))
        self.numero = numero
        self.titular = titular 
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print('O saldo de {} do títular {}'.format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        self.saldo -= valor