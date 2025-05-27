from sae import Agente
from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.recolher import Recolher

class AgenteReativo(Agente):
    def __init__(self):
        comportamento = Recolher()
        controlo=ControloReact(comportamento)
        super().__init__(controlo)

'''Um agente reativo tem o controlo reativo que funciona com base no comportamento.'''