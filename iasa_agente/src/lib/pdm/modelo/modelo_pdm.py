from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    '''Modelo do mundo - representação do problema'''
    @abstractmethod
    def S():
        '''conjunto de estados do mundo'''
    @abstractmethod
    def A(a):
        '''conjunto de acções possíveis no estado'''

    @abstractmethod
    def T(s,a,sn):
        '''probabilidade transição'''

    @abstractmethod
    def R(s,a,sn):
        '''recompensa'''

    @abstractmethod
    def suc(s, a):
        '''os estados seguinte de acordo com a ação recebida'''