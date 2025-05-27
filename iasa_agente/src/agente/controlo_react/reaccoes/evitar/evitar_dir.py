from ecr.reaccao import Reaccao
from agente.controlo_react.reaccoes.evitar.estimulo_obst import EstimuloObst

class EvitarDir(Reaccao):
    def __init__(self, direcao, resposta):
        self.__direcao=direcao
        self.__resposta=resposta
        estimulo=EstimuloObst(self.__direcao)
        super().__init__(estimulo, self.__resposta)