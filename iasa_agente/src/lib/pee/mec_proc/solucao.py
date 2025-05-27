from pee.mec_proc.passo_solucao import PassoSolucao
class Solucao():

    '''Uma solução é, geramente, o resultado final de uma procura.
    Ela corresponde à sequência de nós (estados e operadores) no ramo da
    árvore de procura que contém o nó correspondente ao estado objetivo.'''

    '''Método que permite que a classe Solucao seja iterável e que retorna
    um iterador sobre a lista de passos.'''
    def __iter__(self):
        return iter(self.__passos)
    
    '''Método que indexa a lista de passos.'''
    def __getitem__(self,index):
        return self.__passos[index]
    
    def __init__(self, no_final):
        # self.no_final = no-_final-> Minha solução
        self.__no_final=no_final
        self.__passos=[]
        no=self.__no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0,passo)
            no=no.antecessor

    '''
    19 Armazena-se o nó final da solução.
    20 Constroi-se os passos, ou seja, a estrutura interna da solução. Quando
    incializa-se o nó final é necessario adicionar os passos da solução.
    21 Defini-se um nó temporário para iterar sobre a lista.
    22 Neste ciclo while, anda-se para trás e verifica-se se o nó tem antecessor.
    23 Cria-se um PassoSolucao para cada nó antecessor e operador aplicado ao próprio nó.
    24 Insere-se o passo no início. Não se utiliza o append pois este método adiciona no fim.
    25 A variável nó é então atualizada para nó antecessor.


    CORREÇÃO DA IMPLEMENTAÇÃO:
    Na primeiro solução, o no final era definido como público. No entanto
    Logo o nó final é privado. Deve se adicionar '__' depois do self.
    '''

    '''A dimensão de uma solução traduz-se na profundidade do nó final da solução.'''
    @property
    def dimensao(self):
        dimensao=self.__no_final.profundidade
        return dimensao
    
    '''Retorna o custo acumulado do nó final.'''
    @property
    def custo(self):
        custo=self.__no_final.custo
        return custo