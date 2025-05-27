from sae.ambiente.direccao import Direccao
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from ecr.comportamento import Comportamento

'''Classe responsável por contar o número de passos do agente reativo.
Quando chegar ao valor 10, o agente move-se para norte.'''
class ContarPassos(Comportamento):
    def __init__(self) :
        self.__passos=0
        self.__resposta=RespostaMover(Direccao.NORTE)

    def ativar(self, percepcao):
        self.__passos+=1
        if self.__passos<=10:
            self.__resposta.ativar(percepcao)

'''Comportamento com memória: produz uma ação em função de uma memória.
As reações não dependem apenas das percepcões, mas também das percepções
anteriores. Para tal, a memória deve ser mantida internamente e atualizada
de acordo com as percepções e reações ativdas.'''