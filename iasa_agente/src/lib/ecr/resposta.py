class Resposta():

    '''Uma resposta representa a geração de uma resposta a um estímulo.'''
    def __init__(self, accao):
        self.accao=accao

    '''Ativa-se a ação de acordo com a sua intensidade.'''
    def ativar(self, percepcao, intensidade=0):
        self.accao.prioridade=intensidade
        return self.accao