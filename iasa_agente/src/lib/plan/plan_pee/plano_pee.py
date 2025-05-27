from plan.plano import Plano

'''No Plano PEE deve-se gerar os passos para atingir o objetivo final.'''
class PlanoPEE(Plano):
    def __init__(self, solucao):
        self.__passos=[passo for passo in solucao]
    '''Armazena os passos numa lista.'''

    def obter_accao(self, estado):
        if self.__passos:
            passo=self.__passos.pop(0)
            if passo.estado==estado:
                return passo.operador
    '''Retorna a próxima ação a ser executada com baso no estado atual do agente.
    Cada vez que se executa, retira-se o passo.'''

    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)
        '''Exibe os passos restantes no plano.'''