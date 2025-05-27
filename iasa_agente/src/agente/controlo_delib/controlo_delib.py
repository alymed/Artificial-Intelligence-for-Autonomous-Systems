from sae.agente.controlo import Controlo
from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from agente.controlo_delib.mec_delib import MecDelib

'''A perceção sem memória não evita situações que já aconteceram no passado e não prevêm o futuro.

Com memória, um sistema é capaz de fazer a comutação em função do passado e presente e tira partido do passado para
evitá-lo e antecipar o futuro de forma a otimizar o objetivo. Este processo é denominado de deliberação:
utiliza mecanismos cognitivos do sistema para otimizar o atingir do objetivo

ARQUITETURA DE AGENTE DELIBERATIVO
-Implementa processos de deliberação, processos deliberativo de racicionio e tomada de decisao (planos de ação).
-São sistemas intencionais, ou seja, operam por concretização de intenções para atingir objetivos explicitamente
representados.

Ao ter várias opções de objetivo, o agente deve escolher qual deseja atingir.

Deliberação e Planeamento, temos de usar o conhecimento:
- que vem da experiência do agente
- de um outro sistema
- de algo que jé tem conhecimento e que o transmite (pessoa que constroi o sistema)'''

class ControloDelib(Controlo):
    def __init__(self, planeador):
        self.__modelo_mundo=ModeloMundo()
        self.__mec_delib=MecDelib(self.__modelo_mundo)
        self.__planeador=planeador
        self.__plano=None
        self.__objetivos=[]

    '''• RACICIONIO AUTOMATIVO: processo que permite resolver problema por simulação interna das
        varias hipoteses do problema.Há uma medida de desempenho, determina o que é bom e avaliação de opçoes

        • RACIOCINIO PRATICO: orientado para a ação, permite o sistem interagir com o ambiente dinamicamnte
            Objetivos a atingir
            Ações realizáveis (norte sul este oeste)
            Representação do mundo (ambiente) (permite o agente ter a informação das ações)

        Resultado do raciocinio --> planos de ação

        • RACIOCÍNIO SOBRE FINS (DELIBERAÇÃO)
        pega na representação interna e comprende as ações possiveis de fins a atingir
        (alvos) e perceber das ações possiveis quais se tornam um objetivo, que guia a
        segunda parte do processo interno'''

    def processar(self, percepcao):
        '''O método processar vai tomar a decisão com base na perceção.
        Observa e atualiza o mundo. Se tiver que reconsiderar, delibera o que fazer e planea como fazer e
        executa a ação. Se não for necessário reconsiderar, simplesmente executa a ação.'''

        self.__assimilar(percepcao)
        if(self.__reconsiderar):
            self.__deliberar()
            self.__planear()
        self.__mostrar()
        accao=self.__executar()
        return accao

    def __assimilar(self, percepcao):
        '''Atualiza-se o modelo do mundo de acordo com a perceção.'''
        self.__modelo_mundo.atualizar(percepcao)

    def __reconsiderar(self):
        '''Retorna true se não existir plano ou o modelo do mundo ter sido alterado.'''
        if(self.__plano is None or self.__modelo_mundo.alterado):
            return True
        return False

    def __deliberar(self):
        '''Atualiza os objetivos do agente'''
        self.__objetivos=self.__mec_delib.deliberar()
    
    def __planear(self):
        '''Ativa o planeador'''
        self.__plano=self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
        
    def __executar(self):
        '''Se existir um plano, executa-se a ação corrente do plano.'''
        if(self.__plano):
            estado=self.__modelo_mundo.obter_estado()
            operador=self.__plano.obter_accao(estado)
            if operador:
                return operador.accao
            else:
                self.__plano=None

    '''Mostra o plano e o mundo modelo'''
    def __mostrar(self):
        # vista=Controlo.__vista
        # self.__plano.mostrar(vista)
        # self.__modelo_mundo.mostrar(vista)

        self.vista.limpar()
        self.__modelo_mundo.mostrar(self.vista)
        if self.__plano:
            self.__plano.mostrar(self.vista)
        if self.__objetivos:
            for objetivo in self.__objetivos:
                self.vista.marcar_posicao(objetivo.posicao)
        
        '''Na primeira implementação, aplicava-se redundância ao definir uma variável
        já existente na classe Controlo e o plano era mostrado sem serem verificados
        alguns aspetos.
        
        Na segunda implementação, em primeiro lugar, a vista anterior é limpa e depois
        é exibido o modelo mundo. Se existir um plano, ele será mostrado. Se houver objetivos,
        a posição de cada um é marcado.'''