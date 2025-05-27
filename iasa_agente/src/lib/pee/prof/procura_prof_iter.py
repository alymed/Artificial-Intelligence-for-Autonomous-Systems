from pee.prof.procura_prof_lim import ProcuraProfLim

'''A Procura em Profundidade Iterativa resolve o problema de escolher um bom valor
para ℓ incrementando todos os valores possíveis até encontrar a solução.

Na procura em profundidade iterativa, utiliza-se a procura em profundidade
com limite até ao limite de profundidade com um passo igual ao incremento.
Se existir uma solução ela é retornada.'''

class ProcuraProfIter(ProcuraProfLim):
    def procurar(self,problema, inc_prof, limite_prof=500):
        for profundidade in range (0, limite_prof+1, inc_prof):
            self.prof_max=profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao

'''
12 Ciclo for que itera sobre as profundidades começando de 0 até ao limite de
profundidade inclusive (limite_prof+1).
13 Defini-se a profundidade máxima com o valor da profundidade atual.
14 Chama-se o método procurar que tentará encontrar uma solução dentro da
profundidade máxima.
15 Se uma solução for encontrada,
16 Retorna-se a solução.'''