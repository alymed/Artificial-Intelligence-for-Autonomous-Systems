from plan.planeador import Planeador
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from pdm.pdm import PDM
from plan.plan_pdm.plano_pdm import PlanoPDM

class PlaneadorPDM(Planeador):
    def __init__(self, gama=0.85, delta_max=1):
        self.__gama=gama
        self.__delta_max=delta_max

    def planear(self, modelo_plan, objetivos):
        if objetivos:
            modelo_pdm=ModeloPDMPlan(modelo_plan,objetivos)
            pdm=PDM(modelo_pdm,self.__gama,self.__delta_max)
            utilidade, politica=pdm.resolver()
            return PlanoPDM(utilidade,politica)
        
        '''Se houver objetivos, instancia-se as classes ModeloPDMPlan
        e PDM. Desta forma, chama-se o método resolver que retorna
        a utilidade esperada e a política ótima. Um plano PDM com a
        utilidade e política é retornada.'''