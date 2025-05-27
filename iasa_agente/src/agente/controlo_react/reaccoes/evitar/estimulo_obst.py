from ecr.estimulo import Estimulo

'''A classe EstimuloObst é responsável por gerar a intensidade da ação
tomada por um agente quando deparado com um obstáculo.'''
class EstimuloObst(Estimulo):
    def __init__(self, direcao, intensidade=1):
        self.__direcao=direcao
        self.__intensidade=intensidade
    
    '''Caso exista contacto com obstáculo, retorna uma intensidade 1.
    Caso contrário, retorna intensidade 0.'''
    def detetar(self, percepcao):
        if percepcao.contacto_obst(self.__direcao):
            return self.__intensidade
        else: return 0