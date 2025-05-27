from pee.mec_proc.fronteira import Fronteira

'''First In First Out: O primeiro elemento a entrar na
fronteira, será o primeiro elemento a sair da fronteira.'''

class FronteiraFIFO(Fronteira):
    def _inserir(self, no):
        self._nos.insert(0,no)
        '''Os novos nós a inserir são adicionados no início
        da lista de forma a garantir que o nó mais antigo
        permanece no final da lista e, assim, é o próximo a
        ser removido.'''