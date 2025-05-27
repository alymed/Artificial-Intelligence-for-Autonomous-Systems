from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade

'''A procura melhor-primeiro expande primeiro o nó com o menor valor
h(n), proximidade do objetivo.
Também avalia o percurso dos nós.
A função f representa o custo da solução, >=0.
Conclui-se que quanto maior o custo, pior a solução.
    
Este método ordena os nós na fronteira de exploração por ordem crescente
de custo. Quanto menor o custo, melhor o nó.'''

class ProcuraMelhorPrim(ProcuraGrafo):
    def __init__(self, avaliador):
        self._avaliador=avaliador
        super().__init__(FronteiraPrioridade(self._avaliador))

    def _manter(self, no):
        return super()._manter(no) or no.custo<self._explorados[no.estado].custo
    '''Este método decide ou não se o nó é mantido de acordo com a lógica do
    método manter de ProcuraGrafo ou se o seu custo for menor que o custo do
    nó explorado com o mesmo estado.'''