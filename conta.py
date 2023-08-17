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
    
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite 
        return valor_a_sacar <= valor_disponivel_a_sacar
    
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {}  passou o limite".format(valor))
    
    def transfere(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
