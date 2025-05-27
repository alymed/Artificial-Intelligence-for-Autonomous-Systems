from abc import ABC, abstractmethod

'''Interface que representa o estado atual do sistema, os estados válidos e os operadores disponíveis.'''
class Planeador(ABC):
    @abstractmethod
    def planear(modelo_plan, objetivos):
        ''''''