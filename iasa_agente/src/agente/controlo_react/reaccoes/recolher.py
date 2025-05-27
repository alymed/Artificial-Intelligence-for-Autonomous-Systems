from ecr.hierarquia import Hierarquia
from agente.controlo_react.reaccoes.explorar.explorar import Explorar
from agente.controlo_react.reaccoes.contar_passos import ContarPassos
from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst

class Recolher(Hierarquia):
    '''Recolher é um comportamento composto que tem como objetivo recolher alvos.
    Para tal, o agente vai aproximar alvos, evitar obstáculos e explorar.
    É concretizado através dos sub-comportamentos, logo herdará a classe Hierarquia.'''
    def __init__(self):
        comportamentos=[AproximarAlvo(), EvitarObst(), Explorar()]
        super().__init__(comportamentos)
    