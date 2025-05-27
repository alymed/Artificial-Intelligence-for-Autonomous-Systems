from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

'''Em python @dataclass é módulo decorador que fonece funções que
adicionam automaticamente métodos especiais gerados.'''
@dataclass
class PassoSolucao:
    estado: Estado
    '''Instância 'Estado' que representa a configuração do problema
    num determinado passo.'''

    operador: Operador
    '''Instância 'Operador' que representa a ação aplicada para
    atingir o estado.'''

    '''A classe PassoSolucao representa o passo em uma solução de um
    problema, configuração do problema. Cada passo consiste num estado
    e no operador aplicado para alcançar o estado.'''