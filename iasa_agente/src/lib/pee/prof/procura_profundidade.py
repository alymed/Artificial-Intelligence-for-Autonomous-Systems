from pee.mec_proc.mecanismo_procura import MecanismoProcura
from pee.prof.fronteiraLIFO import FronteiraLIFO

'''A Procura em Profundidade é um mecanismo de procura que expande em primeiro
lugar o nó mais profundo da fronteira, ou seja, o últimos nós gerados,
aumentando a profundidade do ramo corrente de procura. Por este motivo, é
utilizada a fronteira LIFO'''
class ProcuraProfundidade(MecanismoProcura):
    def __init__(self):
        self._fronteira=FronteiraLIFO()
        super().__init__(self._fronteira)
   
    def _memorizar(self,no):
        self._fronteira._inserir(no)  