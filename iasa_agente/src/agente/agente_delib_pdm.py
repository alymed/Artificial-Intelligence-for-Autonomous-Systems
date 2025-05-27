from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from agente.controlo_delib.controlo_delib import ControloDelib
from sae.agente.agente import Agente

class AgenteDelibPDM(Agente):
    def __init__(self):
        planeador= PlaneadorPDM()
        controlo= ControloDelib(planeador)
        super().__init__(controlo)

    '''Um AgenteDelibPDM é controlado por um Controlador Deliberativo e
    planeado por um Planeador de Processo de Decisões de Markov.'''