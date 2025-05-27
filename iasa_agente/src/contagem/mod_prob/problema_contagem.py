from mod.problema import Problema
from mod_estado.estado_contagem import EstadoContagem
from mod_oper.operador_incremento import OperadorIncremento

'''Esta classe define um problema de contagem cujo objetivo é atingir ou superar
um valor final recebido.'''
class ProblemaContagem(Problema):
    def __init__(self, valor_inical, valor_final, incrementos):
        self.__valor_final=valor_final
        super().__init__(EstadoContagem(valor_inical), [OperadorIncremento(incremento)for incremento in incrementos])

    '''Este método diz se o estado recebido é um objetivo.
    Restudar o valor de um estado se esse antingir um valor igual ou superior
    ao valor final.'''
    def objetivo(self, estado):
        return estado.get_valor >= self.__valor_final