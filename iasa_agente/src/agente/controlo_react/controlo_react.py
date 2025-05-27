from sae import Controlo
'''Na arquitetura de um agente reativo, um controlo reativo consiste no processaemnto das
percepções com base no comportamento do agente'''
class ControloReact(Controlo):
    def __init__(self, comportamento):
        self.__comportamento=comportamento
        self.mostrar_per_dir=True
        # Mostra a informação sensorial do agente, a percepção direcional dos vários sensores

    def processar(self, percepcao):
        return self.__comportamento.ativar(percepcao)