from mod.estado import Estado

'''Estende a classe Estado e representa a posição do agente.'''
class Estado(Estado):
    def __init__(self, volume):
        self.__volume=volume 
        '''Posição do agente é privada e só pode ser acedida
        para leitura.'''

    def id_valor(self):
        return self.__volume.__hash__()
    '''Retorna o valor hash do atributo posição.'''
    
    @property
    def volume(self):
        return self.__volume