from plan.planeador import Planeador
from pee.melhor_prim.procura_informada import ProcuraInformada
from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.plano_pee import PlanoPEE

'''Planeador Procura em Espaço de Estados cria um plano de ações que permite o agente
seguir o percurso correto para um objetivo.'''
class PlaneadorPEE(Planeador):
    def __init__(self):
        self.__mec_pee=ProcuraAA()

    '''Se houver objetivos a cumprir, o estado final será o objetivo mais proximo.'''
    def planear(self, modelo_plan, objetivos):
        if objetivos:
            estado_final = objetivos[0]
            problema=ProblemaPlan(modelo_plan, estado_final)
            heuristica =HeurDist(estado_final)
            solucao=self.__mec_pee.procurar(problema, heuristica)
            if solucao:
                return PlanoPEE(solucao)
            
'''
15 Se há objetivos,
16 Seleciona-se o primeiro objetivo
17 e cria-se uma instancia ProblemaPlan.
18 Define-se a heurística que calcula a distância até ao objetivo final
19 e a solução encontrada através do mecanismo de procura.
20 Se esta solução existir,
21 retorna-se uma instância PlanoPEE com a mesma.
'''