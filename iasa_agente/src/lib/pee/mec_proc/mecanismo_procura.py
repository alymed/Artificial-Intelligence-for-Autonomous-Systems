from abc import ABC, abstractmethod
from pee.mec_proc.solucao import Solucao
from pee.mec_proc.no import No

'''A procura em espaço de estados é definida como uma técnica de resolução
de problemas onde o objetivo é encontrar uma sequência de situações e
ações até atingir uma situação final, ou objetivo.

O algoritmo de busca verifica vários caminhos a partir do estado inicial,
tentando encontrar um caminho que atinja um estado objetivo. Se não forem
encontrados estados sucessores, o processo de procura termina com a indicação
de que não existe solução.

Um método de procura pode ser classificado como:
    -->completo: caso exista, a solução é garantida;
    -->ótimo: garante que a solução encontrada é a melhor;
    --> complexo:
        -no tempo: tempo necessário para encontrar uma solução
        -no espaço: memória necessária para encontrar uma solução

Um mecanismo de procura consiste na exploração dos estados.
Será verificado se o estado atual do sistem corresponde '''
class MecanismoProcura(ABC):
    def __init__(self, fronteira):
        self.fronteira=fronteira
        '''O mecanismo de procura trabalha com diferentes tipos de fronteiras.'''
    
    '''Este método trata da construção de estrutura de dados sem memória.
    Implementa-se atarvés de uma programação incremental.'''
    def _iniciar_memoria(self):
        self.fronteira.iniciar()
        '''Iniciar a fronteira'''

    '''Método abstrato onde o nó é mantido em memória do sistema'''
    @abstractmethod
    def _memorizar(no):
        ''''''

    '''Núcleo do mecanismo'''
    def procurar(self,problema):
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not self.fronteira.vazia:
            no=self.fronteira.remover()
            if problema.objetivo(no.estado):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)

    '''
    34 Inicia-se a memória.
    35 Cria-se o nó que corresponde ao estado incial do problema e
    36 ele é memorizado, visto que pode ter vários significados dependemente do procura.
    37 Enquanto a fronteira não estiver vazia,
    38 remove-se o nó da fronteira.
    39 Se o estado do nó é um objetivo do problema, 
    40 retorna-se a solução com o nó
    41 Caso contrário, para cada nó sucessor gerado no expandir, 
    42 é memorizado.'''

    '''Método responsável opr expandir os nós.'''
    def _expandir(self, problema, no):
        sucessores=[]
        estado=no.estado
        for operador in problema.operadores:
            estado_sucessor=operador.aplicar(estado)
            if estado_sucessor is not None:
                custo=no.custo+operador.custo(estado, estado_sucessor)
                no_sucessor = No(estado_sucessor, operador, no, custo) 
                sucessores.append(no_sucessor)
        return sucessores
    
    '''
    63 Inicia-se a lista de sucessores vazia.
    64 Recebe-se o estado do nó.
    65 Para cada operador do problema
    66 gera-se o estado sucessor.
    67 Se o tal estado não for do tipo None,
    68 calcula-se o custo do nó,
    69 cria-se o nó sucessor 
    70 e adiciona-se à lista de sucessores.
    71 No fim, retorna-se os nós sucessores.'''