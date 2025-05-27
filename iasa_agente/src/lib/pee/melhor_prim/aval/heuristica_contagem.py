from pee.melhor_prim.aval.heuristica import Heuristica

'''A classe HeuristicaContagem herda a classe Heuristica e é 
responsável por definir uma heurística baseada na ddiferença entre
um valor final e o valor do estao atual.

É utilizado no módulo contagem_p3 onde o objetivo é atingir um valor
específico a partir de valores atuais.'''

class HeuristicaContagem(Heuristica):
    def __init__(self,valor_final=9):
        self.__valor_final = valor_final

    def h(self, estado):
        return abs(self.__valor_final-estado.id_valor())