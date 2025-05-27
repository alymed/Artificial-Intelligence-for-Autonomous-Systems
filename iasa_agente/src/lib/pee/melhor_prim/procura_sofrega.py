from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.aval.avaliador_sof import AvaliadorSof

'''A procura sôfrega é responsável pela minimização da estimativa do custo.
Logo tem uma menor complexidade computacional.

Herda a ProcuraInformada.'''

class ProcuraSofrega(ProcuraInformada):
    def __init__(self):
        super().__init__(AvaliadorSof())
