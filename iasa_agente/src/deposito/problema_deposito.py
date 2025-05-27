from mod.problema import Problema
from encher import Encher
from vazar import Vazar
from estado import Estado

class ProblemaDeposito(Problema):
    def __init__(self, volume_inicial, volume_final):
        self.__volume_final=volume_final

        super().__init__(Estado(volume_inicial), [Encher(2),Encher(3),Vazar(2), Vazar(3)])

        
    def objetivo(self, estado):
        # return estado.__volume == self.__volume_final
        return estado.volume == self.__volume_final