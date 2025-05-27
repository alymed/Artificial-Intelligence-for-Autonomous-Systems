from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.aval.avaliador_aa import AvaliadorAA

'''A procura A* segue uma heurística admissível, onde expande o nó com um
percurso ótimo, ou seja, minimiza o custo global do nó ao objetivo.

A classe ProcuraAA herda a classe ProcuraInformada que por sua vez define
uma estrutura de mecanismo de procura.'''
class ProcuraAA(ProcuraInformada):
    def __init__(self):
        super().__init__(AvaliadorAA())

    '''Inicializa-se a fronteira e o dicionário de nós explorados,
    especificando a utilização de um avaliador A* que calcula a prioridade
    do nó.'''