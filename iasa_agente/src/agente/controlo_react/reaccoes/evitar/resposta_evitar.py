from agente.controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae.ambiente.direccao import Direccao
from random import choice

'''Esta classe gera a resposta que o agente acionará com o objetivo de evitar um obstáculo'''
class RespostaEvitar(RespostaMover):
    def __init__(self, dir_inicial=Direccao.ESTE):
        self.__dir_inicial=dir_inicial
        super().__init__(self.__dir_inicial)
    
    def ativar(self, percepcao, intensidade):
        '''super().ativar(percepcao,intensidade) --> código antigo'''  
        if percepcao.contacto_obst(self.accao.direccao):
            direcao_livre=self.__direcao_livre(percepcao)
            if direcao_livre:
                self.accao.direccao=direcao_livre
            else:
                return None
        return super().ativar(percepcao,intensidade)
    
    '''No segundo código, ao contrário da primeira versão, a resposta só será ativada após várias verificações:
    Se '''

    def __direcao_livre(self,percepcao):
        direcoes_livres=[direcao for direcao in Direccao if not percepcao.contacto_obst(direcao)]
        if direcoes_livres:
            return choice(direcoes_livres)

        '''for direcao in Direccao:
            if percepcao.contacto_obst(direcao):
                direcoes =list(Direccao)
                direcao = choice(direcoes)
            self.ativar(percepcao)
        return direcao -->  código antigo'''