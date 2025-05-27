from plan.plan_pee.planeador_pee import PlaneadorPEE
from agente.controlo_delib.controlo_delib import ControloDelib
from sae.agente.agente import Agente

class AgenteDelibPEE(Agente):
    def __init__(self):
        planeador= PlaneadorPEE()
        controlo= ControloDelib(planeador)
        super().__init__(controlo)

    '''Um AgenteDelibPEE é controlado por um Controlador Deliberativo e
    planeado por um Planeador de Procura em Espaços de Estados.'''