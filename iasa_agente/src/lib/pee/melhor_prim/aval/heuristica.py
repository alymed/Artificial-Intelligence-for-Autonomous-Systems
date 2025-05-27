from abc import ABC, abstractmethod

'''A classe Heuristica é uma classe abstrara que
serve de interface para os inúmeros tipos de
heurísticas que podem ser usadas nos diferentes
tipos de procura.'''
class Heuristica(ABC):
    @abstractmethod
    def h(self, estado):
        ''''''