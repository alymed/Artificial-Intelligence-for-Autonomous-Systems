from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

'''AvaliadorAA herda AvaliadorHeuristico'''
class AvaliadorAA(AvaliadorHeur):
    def prioridade(self,no):
        return no.custo + self._heuristica.h(no.estado)
    '''A propriedade do nó é a soma do seu custo acumulado com a
    heurística do custo para alcançar o objetivo.'''