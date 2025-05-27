from pdm.mec_util import MecUtil
'''Processos de Decisão de Markov
Esta classe implementa um mecanismo que resolve PDM.
É calculada a política e utilidade dos estados.'''

class PDM():
    def __init__(self, modelo, gama, delta_max):
        self.__modelo=modelo
        self.__mec_util=MecUtil(self.__modelo,gama, delta_max)

    def politica(self,U):
        politica={}
        for s in self.__modelo.S():
            accoes = self.__modelo.A(s)
            if accoes:
                politica[s]=max(accoes, key=lambda a: self.__mec_util.util_accao(s,a,U))
        return politica
    '''Calcula a política ótima para cada estado com base
    na utilidade dos estados.'''

    def resolver(self):
        utilidade=self.__mec_util.utilidade()
        politica=self.politica(utilidade)
        return utilidade, politica
    '''Retorna um tuplo da utilidade e a política.'''