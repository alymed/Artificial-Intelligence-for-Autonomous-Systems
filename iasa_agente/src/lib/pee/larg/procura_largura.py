from pee.mec_proc.procura_grafo import ProcuraGrafo
from pee.larg.fronteira_fifo import FronteiraFIFO

'''PROCURA EM LARGURA
O nó raiz é o primeiro expandido, depois todos os sucessores do
nó raiz são expandidos, em seguida são expandidos os sucessores
dos sucessores e assim por diante.

ProcuraLargura estende a classe ProcuraGrafo, que por sua vez
estende a classe MecanismoProcura.
Desta forma, a Procura Largura é responsável por construir a
estrutura de dados FIFO sem memória.

A procura em largura é em uma procura em grafo mas que utiliza
a fronteira FIFO'''
class ProcuraLargura(ProcuraGrafo):
    def __init__(self):
        fronteira=FronteiraFIFO()
        super().__init__(fronteira)
