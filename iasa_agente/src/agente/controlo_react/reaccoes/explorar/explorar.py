from random import choice
from sae import Direccao
from ecr.comportamento import Comportamento
from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

class Explorar(Comportamento):
    def direcao_explorar(self):
        direcoes=list(Direccao)
        return choice(direcoes)
    
    def ativar(self,percepcao):
        resposta=RespostaMover(self.direcao_explorar())
        return resposta.ativar(percepcao)
    
    '''A classe Explorar gera uma direção aleatória cuja resposta é retornada através do método
    RespostaMover e ativada dada a percepção recebida.

    Consiste numa sequencia de ativação fixa.
    Não depende de estimulo e retorna a ativação da reposta de um movimento aleatório.'''