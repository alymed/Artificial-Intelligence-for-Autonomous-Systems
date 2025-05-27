package maquest;

import agente.Acao;

//A transição é um acontecimento através do qual o sistema evolui do estado atual para um novo estado
public class Transicao {
    //cada transição tem indicação do proximo estado e da ação executada
    private Acao acao;
    private Estado estadoSucessor;
    public Transicao(Estado estadoSucessor, Acao acao){
        this.acao=acao;
        this.estadoSucessor=estadoSucessor;
    }

    //Visto que o atributo estadoSucessor e acao são do tipo {read only}, o objeto será
    //privado e poderá ser acedido (lido) com o método público getAcao() e getEstadoSucessor(),
    //respetivamente.
    public Acao getAcao(){
        return acao;
    }
    public Estado getEstadoSucessor(){
        return estadoSucessor;
    }
}
