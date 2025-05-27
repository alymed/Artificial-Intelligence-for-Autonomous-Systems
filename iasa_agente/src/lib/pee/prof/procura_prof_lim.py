from pee.prof.procura_profundidade import ProcuraProfundidade

'''A procura em profundidade limitada é fornecido um limite de profundidade,
ℓ, e todos os nós na profundidade ℓ são tratados como se não tivessem
sucessores. Por outras palavras, limita a procura de profundidade.'''
class ProcuraProfLim(ProcuraProfundidade):
    def __init__(self,prof_max=50):
        self.__prof_max=prof_max
        super().__init__()

    '''Expande-se o nó quando a profundidade for menor que a profundidade
    máxima. Depois, cada nó sucessor é inserido na fronteira.'''
    def _expandir(self, problema, no):
        fronteira=[]
        if(no.profundidade<self.__prof_max):
            for no.sucessor in self._expandir(problema, no):
                fronteira._inserir(no)
                return fronteira

    '''Retorna a profundidade máxima.'''
    @property
    def prof_max(self):
        return self.__prof_max

    '''Definição de um método setter para a profundidade máxima.'''
    @prof_max.setter
    def prof_max(self, valor):
        self.__prof_max = valor
        