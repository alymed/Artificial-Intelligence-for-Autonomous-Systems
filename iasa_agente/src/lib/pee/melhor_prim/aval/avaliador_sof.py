from pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

class AvaliadorSof(AvaliadorHeur):
    def prioridade(self, no):
        # super()._heuristica.h(no.estado)         PRIMEIRA SOLUÇÃO
        # return no.__custo + super().prioridade()

        return self._heuristica.h(no.estado)

    '''Na primeira solução, é retornada a soma do custo acumulado com
    a prioridade heurística. No tanto, tal não corresponde a este tipo
    de procura mas sim a A*.
    A implementação correta retorna o valor da função heurística
    aplicada ao estado do nó. Ou seja, retorna a estimativa do custo
    do estado do nó até ao objetivo.'''