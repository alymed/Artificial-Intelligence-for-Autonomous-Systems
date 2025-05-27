from ecr.comport_comp import ComportComp

class Prioridade(ComportComp):
    '''As respostas são selecionadas de acordo com uma prioridade
    dinâmica associada que varia ao longo da execução
    
    À cada ação, existe uma prioridade associada.'''
    
    def selecionar_accao(self, acoes):
        '''Verifica-se a prioridade de cada ação e compara-se os valores, devolvendo o maior.
        Em primeiro lugar, percorro a lista com um for e para cada ação, acedo ao valor da
        prioridade com '.prioridade'. este valor será sempre comparado e o maior será armazenado
        numa varivável que seria depois retornada.'''

        if (acoes):
            funcao_selecao = lambda accao: accao.prioridade
            return max(acoes, key=funcao_selecao)