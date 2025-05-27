from pee.melhor_prim.aval.heuristica import Heuristica
import math

'''A partir do estado recebido, deve antigir estado final.
Calcula-se a distância entre a posição do estado recebido e estado final.'''
class HeurDist(Heuristica):
    def __init__(self, estado_final):
        self.estado_final=estado_final

    def h(self, estado):
        return math.dist(estado.posicao , self.estado_final.posicao)