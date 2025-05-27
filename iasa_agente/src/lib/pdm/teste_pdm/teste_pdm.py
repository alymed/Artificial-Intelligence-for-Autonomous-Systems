from pdm.modelo.modelo_pdm import ModeloPDM
from pdm.pdm import PDM

class Teste(ModeloPDM):
    def S(self):
        return [1,2,3,4,5,6,7]

    def A(self, s):
        return ['<','>'] if s not in [1,7] else []
        
    def T(self, s, a, sn):
        '''verifico ações possiveis'''
        return 1 if s not in [1,7] else 0
        
    def R(self, s, a, sn):
        return 1 if sn==7 else -1 if sn==1 else 0
            
    def suc(s, a):
        return [max(1,s-1) if a=='<' else min(7,s+1)]

    '''instanciar o modelo
    instancia pdm passando o modelo
    utilizar resolver que devolve utilidade e politica
    '''