from ecr.estimulo import Estimulo
from sae.ambiente.elemento import Elemento

class EstimuloAlvo(Estimulo):
    def __init__(self, direcao, gama=0.9):
        self.__gama=gama
        self.__direcao=direcao
        '''Os parâmetros gama e direção são do tipo privado (self.__), tendo o gama um valor
        default e, por esta razão, deve ser o último parâmetro.'''

    def detetar(self, percepcao):
        elemento, distancia, posicao=percepcao[self.__direcao]  # associa-se o estimulo a essa direção'''
        if elemento==Elemento.ALVO:
            intensidade=self.__gama**distancia
        else: intensidade=0
        return intensidade

'''Se exixtir um alvo numa determinada direção,
será retornada uma intensidade com base no seguinte calculo: gama**distancia.
Esta intensidade é função inversa da distância, ou seja, quanto menor a distância menor a intensidade.'''