'''Um import pode ser relativo ou absoluto:
relativo --> from .modulo (pasta atual) import A; from ..modulo (pasta acima) import B
absoluto --> from modulo (pasta absoluta) import C'''

from abc import ABC, abstractmethod

'''Numa arquitetura de agente reativos, o comportamento do sistema é gerado
de forma reativa, ou seja, baseado na relação entre estímulos e respostas.
O agente reativo pode ser definido por um conjunto de reações, também
designados comportamentos.

Um comportamento consiste em reações que se relacionam entre sim e produzem
uma ação. Por outras palavras, relaciona padrões de perceção com padrões de ação.


Um comportamento pode ser:
- simples: reação;
- composto: constituído por um conjunto de comportamentos; agrega varios
comportamentos.'''

#Comportamento simples
class Comportamento(ABC):
    @abstractmethod
    def ativar(percepcao):
        ''''''

'''Um comportamento simples representa uma associação estímulo-resposta
   Com uma determinada perceção, a reação será ativada, o estímulo a
   detetará e calculará a sua intensidade. De acordo com esta, ativar-se-á
   uma resposta que vai ser acionada.'''