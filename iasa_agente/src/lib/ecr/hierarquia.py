from ecr.comport_comp import ComportComp

class Hierarquia(ComportComp):
    '''Na seleção de uma ação, os comportamentos estão organizados
    numa hierarquia fixa de supressão e substituição.
    
    As ações estão organizadas seguindo uma hierarquia.'''
    
    def selecionar_accao(self, acoes):
        if (acoes):
            return acoes[0]