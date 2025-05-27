from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

'''A procura informada consiste em estratégias de exploração do espaço,
com base no conhecimento do problema de forma a ordenar a fronteira de
exploração.

Esta procura utiliza conhecimento do domínio do problema para guiar a
procura e tem sempre um avaliador heurístico.'''
class ProcuraInformada(ProcuraMelhorPrim):
    def procurar(self, problema, heuristica):
        '''Configurar a heuristica do avaliador.'''
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)
