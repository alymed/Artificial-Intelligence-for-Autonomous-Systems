from abc import ABC, abstractmethod

class Avaliador(ABC):
    @abstractmethod
    def prioridade(self, no):
        ''''''

'''O avaliador define o contrato funcional (interface) de
avaliação da prioridade de um nó para ordenação da fronteira
por prioridade, é concretizado de acordo o tipo de procura.'''