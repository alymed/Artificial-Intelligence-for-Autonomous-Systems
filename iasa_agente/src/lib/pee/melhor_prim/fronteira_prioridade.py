from pee.mec_proc.fronteira import Fronteira
from heapq import heappush, heappop

'''A classe FronteiraPrioridade herda a classe Fronteira.

É utilizada uma fila de prioridade heap que gere os nós.'''
class FronteiraPrioridade(Fronteira):
    def __init__(self, avaliador):
        self._avaliador=avaliador
        '''avaliador é protegido e determina a prioridade dos nós'''

    def _inserir(self, no):
        prioridade=self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))

    '''Este método adiciono um novo nó à heap juntamente com a sua
    prioridade obtida a partir do avaliador.
    
    Heaps são árvores binárias para as quais cada nó tem um valor
    menor ou igual a qualquer um dos seus sucessores.'''
    
    def remover(self):
        _,no = heappop(self._nos)
        return no

    '''Este método remove o nó com a menor prioridade da lista.
    Como a prioridade não é usada, suprimi-se o primeiro argumento
    do tuplo, ou seja, ele é ignorado.'''