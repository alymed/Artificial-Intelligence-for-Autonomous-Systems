from pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim
from pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif

'''A procura de custo uniforme é uma variação da procura melhor primeiro
cuja função é diretamente o custo do percurso até ao nó.
Primeiro são explorados os primeiros percursos com menor custo, garantindo
uma solução de menor custo.'''

class ProcuraCustoUnif(ProcuraMelhorPrim):
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())

    '''Inicializa-se a fronteira e o dicionário de nós explorados,
    especificando a utilização de um avaliador custo uniforme.'''