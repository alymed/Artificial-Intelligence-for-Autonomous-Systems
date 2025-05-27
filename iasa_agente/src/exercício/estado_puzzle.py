from lib.mod.estado import Estado

'''Classe responsável pela idenficação única do objeto em função da informação do estado.'''
class EstadoPuzzle(Estado):
    def __init__(self, configuração):
        self.configuração=configuração  #informação que caracteriza o estado

    '''Define a identificação única do estado em função da sua informação (valor de estado)'''
    def id_valor(self):
        ok=' '
        for a in range(9):
            b=self.configuração[a]*10**a
            ok+=b
        return int(ok)