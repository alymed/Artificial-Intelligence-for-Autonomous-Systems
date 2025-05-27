class MecUtil():
    '''Responsável pelo cálculo de utilidade.
    A utilidade é a expectativa da recompensa acumulada
    futuramente que um agente pode obter.'''
    def __init__(self, modelo, gama, delta_max):
        self.__modelo=modelo
        self.__gama=gama
        self.__delta_max=delta_max
        
    def utilidade(self):
        S,A =self.__modelo.S, self.__modelo.A
        U={s:0.0 for s in S()}

        while True:
            Uant=U.copy()
            delta=0
            for s in S():
                U[s]=max([self.util_accao(s,a,Uant) for a in A(s)], default=0)
                delta=max(delta,abs(U[s]-Uant[s]))
            if delta<=self.__delta_max:
                break
        return U
    
        '''
        11 Obtem-se os estados e as ações possíveis no estado
        no modelo recebido.
        12 A utilidade são todos os estados com 0.0.
        14 Em cada iteração,
        15 guarda-se a utilidade atual numa variável utilidade anterior
        16 e igual-se o delta a zero.
        17 Para casa estado,
        18 calcula-se uma nova utilidade com o máximo de utilidade
        de ações possíveis
        19 e atualiza-se o delta com a maior diferença entre a utilidade
        nova e a utilidade anterior.
        20 Se o delta for menor ou igual ao delta máximo,
        21 a iteração termina.
        22 Utilidade é retornada.
        '''

        '''U={}             
        for s in self.__modelo.S():          #Para cada estado, inicializa-se o
            U[s]=0                           #o valor no dicionário a 0
        while(delta>self.__delta_max):         #enquanto delta for maior que delta_max,
            u_ant=U.copy()                   #faz-se uma réplica da utilidade anterior
            delta=0                          #e iguala-se delta a 0. A seguir, 
            for s in self.__modelo.S():      #para todos os estados,
                U[s]=max([self.util_accao(s,a,u_ant[s]) for a in self.__modelo.A()]) #calcula-se a utilidade máxima entre todas as ações possíveis
                delta=max(delta, abs(U[s]-u_ant[s]))                             #e delta será o máximo entre delta anterior e o valor absoluto da diferença das utilidades atual e anterior do estado
        return U'''
        
    def util_accao(self,s,a,U):
        T, R, suc, gama=self.__modelo.T, self.__modelo.R, self.__modelo.suc, self.__gama
        return sum([T(s,a,sn)*R(s,a,sn)+gama*U[sn]for sn in suc(s,a)])
    
        # sn=self.__modelo.suc(s,a)
        # return sum(self.__modelo.T(s,a,sn)*(self.__modelo.R(s,a,sn)+self.gama*U))
        '''A utilidade refere-se à historia de evolução, ao valor ao longo prazo.
        Este método representa, para cada estado, a sua utilidade.
        Ou seja, a probabilidade multiplicada pela soma da recompensa e da
        utilidade vezes a gama'''

    '''Retorna o delta máximo.'''
    @property
    def delta_max(self):
        return self.__delta_max

    '''Retorna a gama.'''
    @property
    def gama(self):
        return self.__gama
    
    '''Retorna o modelo.'''
    @property
    def modelo(self):
        return self.__modelo