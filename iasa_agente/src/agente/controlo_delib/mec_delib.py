from sae.ambiente.elemento import Elemento
class MecDelib():
    '''Mecanismo Deliberativo modelariza o processo.'''
    def __init__(self, modelo_mundo):
        self.__modelo_mundo=modelo_mundo

    '''O método deliberar gerará os objetivos do agente.'''
    def deliberar(self):
        # objetivos=[]
        # for estado in self.__modelo_mundo.__estados:
        #     elemento=self.__modelo_mundo.obter_elemento(estado)
        #     if elemento is self.__modelo_mundo.elementos.ALVO:
        #         objetivos.append(elemento)
        # return objetivos

        objetivos=[estado for estado in self.__modelo_mundo.obter_estados()
                   if self.__modelo_mundo.obter_elemento(estado)==Elemento.ALVO]
        if objetivos:
            objetivos.sort(key=self.__modelo_mundo.distancia)
            return objetivos
        
        '''É criada uma lista de objetivos para quando o elemento obtido a partir
        do estado é um alvo. Se forem definidos objetivos, eles são ordenado de
        acordo com a distância entre as posições dos estados.
        
        Na primeira implementação, não estava incluida a ordenação da lista pela distância.'''