from ecr.prioridade import Prioridade
from agente.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from sae.ambiente.direccao import Direccao

class AproximarAlvo(Prioridade):
    def __init__(self):
        comportamentos = [AproximarDir(Direccao.NORTE), AproximarDir(Direccao.SUL), 
                          AproximarDir(Direccao.ESTE), AproximarDir(Direccao.OESTE)]
        
        comportamentos =[AproximarDir(direcao) for direcao in Direccao]
        super().__init__(comportamentos)

'''Esta classe é responsável por aproximar o agente do alvo mais próximo.
Para produzir esta ação de aproximação ao alvo mais próximo, utiliza-se o mecanismo
de seleção através da prioridade.'''