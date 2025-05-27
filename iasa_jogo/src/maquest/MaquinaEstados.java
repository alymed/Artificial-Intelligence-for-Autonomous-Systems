package maquest;

import agente.Acao;
import ambiente.Evento;

//Uma Máquina de Estados é um modelo matemático que exibe transições entre vários objetos
public class MaquinaEstados {
    public Transicao transicao;
    private Estado estado;

    public MaquinaEstados(Estado estadoInicial){
        this.estado=estadoInicial;
    }

    //Para processar um evento, geramos uma transição a partir do mesmo.
    //Se esta não for nula, atualizamos o estado pelo estado seguinte
    //correspondente e retornamos a ação respetiva à transição.

    public Acao processar (Evento evento){
        transicao = estado.processar(evento);
        if(transicao!=null){
            estado=transicao.getEstadoSucessor();
            return transicao.getAcao();
        } else {
            return null;
        }
    }
    public Estado getEstado() {
        return estado;
    }
}
