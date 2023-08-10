class Conta:

    def __init__(self, numero, titular, saldo, limite): #função construtora
        print('Construindo um objeto...'.format(self))
        self.__numero = numero
        self.__titular = titular #Atributos com 2 underscore é privado 
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print('O saldo de {} do títular {}'.format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)