"""
Acção do agente
@author: Luís Morgado
"""

from dataclasses import dataclass

from ..ambiente.direccao import Direccao

#_______________________________________________________________________________

@dataclass
class Accao:
    """Representação de acção"""
    direccao: Direccao
    """Direcção de movimento"""
    passo: int = 1
    """Distância de movimento"""
    prioridade: int = 0
    """Prioridade da acção"""

    @property
    def ang(self):
        """
        Ângulo da direcção da acção
        """
        return self.direccao.value

    def __hash__(self):
        """
        Identificação por valor
        """
        return hash(self.direccao)    
  
    def __repr__(self):
        """
        Representação de acção
        """
        return "Accao(%s)" % self.direccao


'''modelação de sistema autonomo inteligente - agente:

agente tem 3 processos principais e um modulo de controlo
-percepcionar recebe informação do ambiente
-atuar pega em info interna do agente, comandos, e transforma em comandos concretos sobre atuadores do sistem
-processar- representa toda a computação interna

modelo deliberativo custo computacional alto, muito complexo
modelo reativo mais simples, menos custos, respostas rápidas


percepção é um agregado de estimulos
vamos fazer associação entre estimulos
uma unica percepção ativa varias respostas

resposta inclui a ação
'''