from abc import ABC, abstractmethod

'''A interface Plano representa os planos de ação que são gerados a partir dos objectivos
a atingir, das acções que o agente é capaz de realizar e do ambiente, determinando o
comportamento do agente'''

class Plano(ABC):
    @abstractmethod
    def obter_accao(estado):
        ''''''

    @abstractmethod
    def mostrar(vista):
        ''''''