from pee.mec_proc.fronteira import Fronteira

'''Last In First Out: O último elemento a entrar na
fronteira, será o primeiro elemento a sair da fronteira.'''

class FronteiraLIFO(Fronteira):
    def _inserir(self, no):
        self._nos.append(no)
        '''Os novos nós a inserir são normalmente
        adicionados no fim da lista.'''