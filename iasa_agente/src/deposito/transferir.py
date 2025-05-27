from mod.operador import Operador

class Transferir(Operador):
    def __init__(self, volume):
        self.__volume=volume

    '''Método que gera o custo de transição do estado ao estado sucessor.'''
    
    def custo(self,estado, estado_suc):
        '''custo do volume transferido'''
        custo=(estado_suc.volume - estado.volume)**2

    #adicionei isso
    @property
    def volume(self):
        return self.__volume