from abc import ABC, abstractmethod

'''Um estimulo é um perceção que define a informação ativadora de uma reação.'''
class Estimulo(ABC):
    @abstractmethod
    def detetar(self, percepcao):
        """..."""