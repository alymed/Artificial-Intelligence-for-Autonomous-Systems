from transferir import Transferir
class Encher(Transferir):
    def __init__(self, volume):
        super().__init__(volume)
    # especializa o operador transfeiri

    def aplicar(self, estado):
        # return estado.__volume+self.__volume
        return estado.volume+self.volume

        '''adiciona ao volume do estado o volume do operador
        volume q o estado tinha mais o volume do operador'''