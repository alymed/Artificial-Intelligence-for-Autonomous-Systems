from .comportamento import Comportamento
from abc import abstractmethod

#Comportamento composto
class ComportComp(Comportamento):
    def __init__(self, comportamentos):
        self.__comportamentos=comportamentos

    '''Visto que trata-se de um comportamento composto, para cada comportamento
    da lista de comportamentos, ativa-se o comportamento passando a perceção. Se
    uma ação existir, é adicionada à lista de ações. Depois verifica-se se a lista
    contém alguma ação e, caso tiver, seleciona-se uma ação que será retornada.
    Este mecanismo de seleção determina a ação a realizar em função às respostas
    dos vários comportamentos'''

    def ativar(self, percepcao):
        acoes=[]
        for i in self.__comportamentos: 
            accao=i.ativar(percepcao)
            if(accao is not None):
                acoes.append(accao)

        if acoes:
                return self.selecionar_accao(acoes)
        
    @abstractmethod    
    def selecionar_accao(self, acoes):
        ''' '''