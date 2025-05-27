from mod.operador import Operador
from mod_estado.estado_contagem import EstadoContagem

'''Define um operador que incrementa o valor do estado por um valor recebido.'''
class OperadorIncremento(Operador):

    '''Armazena o atributo privado incremento.'''
    def __init__(self, incremento):
        self.__incremento=incremento

    '''Tranforma o estado num novo estado efetuado sobre
    este estado o incremento devido.'''
    def aplicar(self, estado):
        return EstadoContagem(estado.get_valor+self.__incremento)

    '''Padrão de incremento.
    Não depende do estado nem do estado sucessor.'''
    def custo(self, estado, estado_suc):
        return self.__incremento**2
    
    '''Retorna o incremento.'''
    @property
    def get_incremento(self):
        return self.__incremento