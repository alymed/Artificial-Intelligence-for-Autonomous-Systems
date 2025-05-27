from mod.problema import Problema

'''Define um problema específico no contexto de planejamento de ações
para um agente. Fornece uma interface que verifica se o estado atual é
o objetivo final.'''
class ProblemaPlan(Problema):
    def __init__(self, modelo_plan, estado_final):
        self.modelo_plan=modelo_plan
        estado_incial=self.modelo_plan.obter_estado()
        operadores = self.modelo_plan.obter_operadores()
        self.__estado_final=estado_final
        super().__init__(estado_incial, operadores)

    def objetivo(self, estado):
        if estado == self.__estado_final:
            return True