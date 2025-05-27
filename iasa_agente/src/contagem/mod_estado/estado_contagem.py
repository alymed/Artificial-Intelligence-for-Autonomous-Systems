from mod.estado import Estado
class EstadoContagem(Estado):
    def __init__(self, valor):
        self.__valor=valor

    def id_valor(self):
        return self.__valor

    @property
    def get_valor(self):
        return self.__valor

'''Estado contagem -- mantem a informção do valor da contagem,
ou seja, tem um atributo contagem, propriedade valor do estado,ou seja,
acesso de read only (não se deve mudar a variável).'''