from ecr.hierarquia import Hierarquia
from agente.controlo_react.reaccoes.evitar.resposta_evitar import RespostaEvitar
from agente.controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from sae.ambiente.direccao import Direccao

class EvitarObst(Hierarquia):
    def __init__(self):
        self.__resposta=RespostaEvitar()
        comportamentos=[EvitarDir(direcao, self.__resposta) for direcao in Direccao]
        super().__init__(comportamentos)