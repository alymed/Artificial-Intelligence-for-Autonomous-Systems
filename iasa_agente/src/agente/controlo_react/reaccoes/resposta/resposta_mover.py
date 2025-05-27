from ecr.resposta import Resposta
from sae import Accao

class RespostaMover(Resposta):
    '''Uma resposta encapsula a ação a ser feita. A RespostaMover representa um movimento na direção indicada.'''
    def __init__(self, direcao):
        accao = Accao(direcao)
        super().__init__(accao)