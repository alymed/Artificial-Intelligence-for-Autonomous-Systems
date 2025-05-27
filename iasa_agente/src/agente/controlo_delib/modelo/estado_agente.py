from mod.estado import Estado

'''Estende a classe Estado e representa a posição do agente.'''
class EstadoAgente(Estado):
    def __init__(self, posicao):
        self.__posicao=posicao 
        '''Posição do agente é privada e só pode ser acedida
        para leitura.'''

    def id_valor(self):
        return self.__posicao.__hash__()
    '''Retorna o valor hash do atributo posição.'''
    
    @property
    def posicao(self):
        return self.__posicao