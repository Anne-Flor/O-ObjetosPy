class Cliente:
    def __init__(self, nome):
        self.__nome = nome 

    @property
    def nome(self, ):
        print("Chamando @property nome()")
        return self.__nome.title()
    
    def nome(self, nome):
        print("Chamando setter nomer()")
        self.__nome = nome 