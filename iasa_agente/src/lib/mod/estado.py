from abc import ABC, abstractmethod

'''Os problemas podem ser resolvidos por meios algorítmicos através do raciocínio autómatico.
consiste na capacidade do sistema resolver de forma automática o problema com base no conhecimento do
domínio, produzindo uma solução a partir de várias alternativas.

Este conceito tem como entrada a representação do conhecimento do domínio e retorna as conclusões
que retirou do conhecimento.

O estado representa a configuração na resolução do problema.
Esta classe responsável pela identificação única do objeto em função da informação do estado.'''
class Estado(ABC):

    '''Define a identificação única do estado em função da sua informação (valor de estado)'''
    @abstractmethod
    def id_valor(self):
        ''''''
        
    '''Hashable refere-se à definição de mecanismos de identificação única.
    Este método retorna um inteiro que representa o valor do objeto.'''
    def __hash__(self):
        return self.id_valor()

    '''O método __eq__ define a funcionalidade de um operdador de igualdade.
    É usado para comparar objetos.'''
    def __eq__(self, other):
        if isinstance(other, Estado):
            return self.__hash__()  == other.__hash__()