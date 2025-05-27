class No:

    '''Cada nó corresponde a um estado no espaço de estados.'''
    def __init__(self, estado, operador=None, antecessor=None, custo=0):
        self.estado=estado
        self.operador=operador
        self.antecessor=antecessor
        self.__custo=custo
        ''' Em python, não é possível implementar dois construtores. Desta forma,funde-se
        os dois construtores no que contem mais parâmetros. Então, os parâmetros adicinais
        serão definidos por omissão'''

        if antecessor: 
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0
        '''TROÇO ADICIONADO
        É necessário atualizar a profundidade de um nó ao verificar a existêcia de um antecessor
        caso contrário será sempre zero, o que dificultará depois o processo de procura.
        
        Se existir o antecessor, a profundidade é incrementada.''' 

    '''Método de comparação de nós com base no custo.'''
    def __lt__(self, no):
        return self.__custo < no.__custo

    '''Retorna a profundidade do nó no espaço de estados.'''
    @property
    def profundidade(self):
        return self.__profundidade
    
    '''Retorna o custo do nó no espaço de estados.'''
    @property
    def custo(self):
        return self.__custo