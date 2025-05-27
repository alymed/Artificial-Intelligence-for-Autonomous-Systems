from pee.melhor_prim.aval.avaliador import Avaliador

'''Avaliador Heurístico define um avaliador que utiliza
uma heurística que determina a prioridade dos nós durante
a busca.'''
class AvaliadorHeur(Avaliador):
    def definir_heuristica(self, heuristica):
        self._heuristica=heuristica