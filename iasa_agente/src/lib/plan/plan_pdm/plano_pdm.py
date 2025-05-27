from plan.plano import Plano

class PlanoPDM(Plano):
    def __init__(self, utilidade, politica):
        self.__utilidade=utilidade
        self.__politica=politica
        ''''''

    def obter_accao(self, estado):
        if (self.__politica):
            return self.politica.get(estado)
        ''''''

    def mostrar(self, vista):
        if (self.__politica):
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
            for estado, acao in self.politica.items():
                vista.mostrar_vector(estado.posicao, acao.ang)

        '''utilidade dicionario
        chave estado
        
        para cada tuplo estado valor'''

    @property
    def utilidade(self):
        return self.__utilidade
    
    @property
    def politica(self):
        return self.__politica