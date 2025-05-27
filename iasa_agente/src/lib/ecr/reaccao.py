from ecr.comportamento import Comportamento

'''Uma reação é um comportamento simples que para ser ativada depende do estímulo. É uma associação estimulo - resposta'''
class Reaccao(Comportamento):
    def __init__(self,estimulo,resposta):
        self.__estimulo=estimulo
        self.__resposta=resposta

    def ativar(self, percepção):
        intensidade=self.__estimulo.detetar(percepção)
        if (intensidade>0):
            acao=self.__resposta.ativar(percepção,intensidade)
            return acao
        '''Sobre o estimulo deteta-se a percepção e retorna-se uma intensidade'''