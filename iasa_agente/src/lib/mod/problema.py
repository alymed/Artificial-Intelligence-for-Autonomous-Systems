from abc import ABC, abstractmethod

'''Esta classe define o estado inicial e os operadoes.'''
class Problema(ABC):
    def __init__(self, estado_inicial,operadores):
        self.__estado_inicial=estado_inicial
        self.__operadores=operadores
    
    @abstractmethod
    def objetivo(self, estado):
        ''''''
    
    '''@property é um descritor python que gera o getter de uma variável.'''
    @property
    def operadores(self):
        return self.__operadores
    
    @property
    def estado_inicial(self):
        return self.__estado_inicial
    

'''Um problema é representado através de estruturas mantidas na memória
do sistema. O modelo suporta o raciocínio automático e é representado pelo
estado e pelo operador.'''