from pee.mec_proc.mecanismo_procura import MecanismoProcura

'''A classe ProcuraGrafo é uma subclasse da classe MecanismoProcura
e é responsável por explorar os nós mais antigos.'''
class ProcuraGrafo(MecanismoProcura):
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados={} 
        '''Inicializa-se a fronteira e o dicionário de nós explorados'''
    
    '''Caso o nó seja para ser mantido, será adicionado à fronteira e
    ao dicionário de nós explorados utilizando o estado de nó como key.'''
    def _memorizar(self, no):
        if self._manter(no):
            self.fronteira._inserir(no)
            self._explorados[no.estado]=no
    
    '''Este método indica se o nó é para manter ou não.
    Será mantido se o estado do nó estiver nos explorados.'''
    def _manter(self, no):
        return no.estado not in self._explorados 