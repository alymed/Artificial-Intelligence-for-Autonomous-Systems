from plan.modelo.modelo_plan import ModeloPlan
from pdm.modelo.modelo_pdm import ModeloPDM

'''Combina as funcionalidades das classes ModeloPlan,ModeloPDM'''
class ModeloPDMPlan(ModeloPlan,ModeloPDM):
    def __init__(self, modelo_plan, objetivos, rmax=1000):
        self.__modelo_plan=modelo_plan
        self.__objetivos=objetivos
        self.__rmax=rmax
        self.__transicoes={
            (s,a):a.aplicar(s)
            for s in self.obter_estados()
            for a in self.obter_operadores()
        }

    '''As transições são precalculadas: Para não tarem a ser feitos nos momentos
    em que os métodos são chamados, a variável transições é definida como um
    dicionário de par estado-ação cujo o próximo estado é aplicar a ação ao estado.    
    '''

    '''DELEGAÇÃO. forma de fatorização'''
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        return self.__modelo_plan.obter_estados()

    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    def S(self):
        return self.obter_estados()
    
    '''Retorna a lista de operadores se o estado não for um objetivo'''
    def A(self,s):
        return self.obter_operadores() if s not in self.__objetivos else []
    
    '''Ao ter um ambiente determinista, se a ação pode ser executada a probabilidade é 1.
    se nao, é 0. Para saber se a transição existe, verifica-se na tabela de transições'''
    def T(self, s, a, sn):
        return 1 if self.__transicoes.get((s,a))==sn else 0
    
    '''Modelo de recompensa: se o estado sucessivo for um objetivo, a recompensa é maxima,
    se não é o custo da ação.'''
    def R(self, s, a, sn):
        return self.__rmax if sn in self.__objetivos else -a.custo(s,sn)
    
    '''Gera os próximos estados. O sucessor utilizará as transições já geradas'''
    def suc(self, s, a):
        sn=self.__transicoes.get((s,a))
        return [sn] if sn else []