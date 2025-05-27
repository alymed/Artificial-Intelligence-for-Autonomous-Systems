from abc import ABC, abstractmethod

'''Classe responsável por definir o custo de transição do estado.
É aplicado ao estado e gera um novo.
Representa a ação que tranformará o estado.'''

class Operador(ABC):

    '''Método de aplicação ao estado'''
    def aplicar(self, estado):
        ''''''

    '''Método que gera o custo de transição do estado ao estado sucessor.'''
    @abstractmethod
    def custo(self,estado, estado_suc):
        ''''''