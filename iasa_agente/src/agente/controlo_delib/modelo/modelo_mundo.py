from sae import Elemento
from sae import Direccao
from agente.controlo_delib.modelo.operador_mover import OperadorMover
import math
from plan.modelo.modelo_plan import ModeloPlan
from agente.controlo_delib.modelo.estado_agente import EstadoAgente

'''O modelo do mundo é a representação interna do ambiente.'''
class ModeloMundo(ModeloPlan):
    def __init__(self):
        self.elementos=None
        self.__estado=None
        self.__estados=[]
        self.__operadores=[]

    '''Estado atual do agente'''
    def obter_estado(self):
        return self.__estado
    
    '''Lista de estados do mundo para várias posições'''
    def obter_estados(self):
        return self.__estados
    
    '''Conjunto de operadores que o agente conhece'''
    def obter_operadores(self):
        return self.__operadores
    
    '''Elemento do mundo. Acede ao dicionário de elementos e indica a posição no dicionário.'''
    def obter_elemento(self,estado):
        # posicao=estado.posicao
        # elemento=self.elementos[posicao]  
        return self.elementos.get(estado.posicao)
    '''Na primeira implementação, é utilizada a posição do estado para aceder ao
        elemento através da indexação. No entanto, não é uma variável válida para tal.
        Logo, é utilizado a função get() que retorna o valor do item com base numa
        chave específica, neste caso estado.posicao.'''

    '''Calcula distância entre a posição do estado recebido e posição atual do agente.'''
    def distancia(self, estado):
        return math.dist(estado.posicao,self.__estado.posicao)
    
    '''Atualiza o modelo com base na perceção.'''
    def atualizar(self,percepcao):
        # self.__estados=percepcao.posicao
        self.__estados=[EstadoAgente(posicao) for posicao in percepcao.posicoes]
        for estado in self.__estados:
            if estado.posicao==percepcao.posicao:
                self.__estado=estado

        self.__operadores=[OperadorMover(self,direcao) for direcao in Direccao]

        self.elementos=percepcao.elementos
        self.__recolha=percepcao.recolha

    '''A variável consiste num array de posições da perceção.'''

    def mostrar(self, vista):
        for posicao, elemento in self.elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)
        '''Para cada elemento nas diferentes posições, verifica-se se é um alvo ou obstáculo.
        Se for o caso, o elemento será marcado. Depois de percorrer todos os elementos,
        marca-se a posição correspondente ao estado.'''

    '''Verifica se o mundo foi alterado ou não.'''
    @property
    def alterado(self):
        return self.__recolha