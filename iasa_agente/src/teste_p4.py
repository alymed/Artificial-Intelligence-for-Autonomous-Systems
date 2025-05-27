from agente.agente_delib_pee import AgenteDelibPEE as Agente
# from agente.agente_delib_pdm import AgenteDelibPDM as Agente
from sae import Simulador

#Simulador
Simulador(1, Agente()).executar()