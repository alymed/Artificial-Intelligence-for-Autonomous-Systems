from transferir import Transferir
class Vazar(Transferir):
    def __init__(self, volume):
        super().__init__(volume)

    def aplicar(self, estado):
        return estado.__volume-self.__volume