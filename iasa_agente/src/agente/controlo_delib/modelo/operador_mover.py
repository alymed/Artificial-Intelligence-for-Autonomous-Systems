from mod.operador import Operador
from sae.agente.accao import Accao
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
import math
    
'''A classe OperadorMover estende Operador e é responsável por simular da acção
(movimento), ou seja, as transformações do estado, por translação geométrica'''
class OperadorMover(Operador):
    def __init__(self, modelo_mundo, direcao):
        self.__modelo_mundo=modelo_mundo
        self.__accao=Accao(direcao)
        '''Inicializa-se a ação, a partir da direção, e o modelo do mundo
        onde a ação é executada.'''

    def aplicar(self, estado):
        angulo=self.__accao.ang
        passo=self.__accao.passo
        dx=int(passo*math.cos(angulo))
        dy=int(-passo*math.sin(angulo))
        x=round(estado.posicao[0]+dx)
        y=round(estado.posicao[1]+dy)
        posicao=(x,y)
        estado_suc=EstadoAgente(posicao)
        if (estado_suc in self.__modelo_mundo.obter_estados()):
            return estado_suc
        else: return None
    '''Gera-se um novo estado por translação.
    Retira-se o ângulo e o passo da ação e calcula-se as coordenadas x e y da
    posição. Esta posição servirá para gerar o próximo estado que será retornado
    apenas se fizer parte dos estados do modelo do mundo.'''

    '''O custo depende da distância entre as posições atual e sucessora.'''
    def custo(self, estado, estado_suc):
        return math.dist(estado.posicao, estado_suc.posicao)

    @property
    def ang(self):
        return self.__accao.ang
    @property
    def accao(self):
        return self.__accao
    
