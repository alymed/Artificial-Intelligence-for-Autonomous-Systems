from pee.melhor_prim.aval.avaliador import Avaliador

'''O Avalidador de Custo Uniforma define a prioridade do nó como simplesmente
o custo necessário para alcançar o nó a partir do estado incial.
Desta forma, assegura-e que o nó com menor custo é expandido e assim chega-se
a uma solução ótima.'''
class AvaliadorCustoUnif(Avaliador):
    def prioridade(self, no):
        return no.custo 
    '''É importante notar que a propriedade do nó 'custo' não é privado.'''