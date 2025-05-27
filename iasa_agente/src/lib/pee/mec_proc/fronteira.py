from abc import ABC, abstractmethod

'''Uma fronteira representa uma estrutura de dados cujo critério de
ordenação estabelece a estratégia de procura.'''
class Fronteira(ABC):

    '''Ao chamar o método iniciar() evita-se redundância no código,
    uma vês que tem a mesma função que o __init__'''
    def __init__(self) :
        self.iniciar() 

    '''Inicializa a lista de nós'''
    def iniciar(self):
        self._nos=[]

    '''Método abstrato que insere um nó à fronteira'''
    @abstractmethod
    def _inserir(_nos):
        ''''''

    '''Remove a fronteira'''
    def remover(self):
        if(self.vazia):
            return None
        else: 
            return self._nos.pop(0)

    '''Propriedade booleana que indica se a fronteira está vazia'''
    @property
    def vazia(self):
        vazia=len(self._nos)
        return vazia == 0
    
    '''Retorna a dimensão do nó'''
    @property
    def dimensao(self):
        dimensao=len(self._nos)
        return dimensao