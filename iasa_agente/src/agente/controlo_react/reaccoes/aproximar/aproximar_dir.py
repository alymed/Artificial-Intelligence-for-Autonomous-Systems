from ecr.reaccao import Reaccao
from agente.controlo_react.reaccoes.aproximar.estimulo_alvo import EstimuloAlvo
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

class AproximarDir(Reaccao):
    def __init__(self,direcao):
        estimulo = EstimuloAlvo(direcao)
        resposta = RespostaMover(direcao)
        super().__init__(estimulo,resposta)

    '''Esta classe representa uma associação estimuloAlvo - respostaMover
    A cada direção esta associada uma reação.
    As quatro reações são definidas por prioridade (a prioridade é inversamente proporcional à distância)'''