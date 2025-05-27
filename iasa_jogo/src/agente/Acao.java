package agente;

import ambiente.Comando;

public class Acao {
    private Comando comando; //A classe Acao implementa a classe Comando
    //Ao caracterizar o atributo com uma visibilidade privada, tornamo-lo
    // inacessível à outras partes do sistema.

    //A ação é criada por um comando.
    public Acao(Comando comando){
        this.comando=comando;
    }
    //Visto que o atributo comando é do tipo {read only}, o objeto será
    //privado e poderá ser acedido (lido) com o método público getComando().
    public Comando getComando(){
        return comando;
    }
}
