package maquest;

import agente.Acao;
import ambiente.Evento;

import java.util.HashMap;
import java.util.Map;

//Um estado é a representação da situação de evoluação de um sistema
public class Estado {
    public String nome; //nome que identificar melhor o estado
    private Map<Evento, Transicao> transicoes; //conjunto de transições asscociadas

    public Estado(String nome){
        this.nome=nome;
        transicoes=new HashMap<Evento,Transicao>();
    }

    public Transicao processar (Evento evento){
        return transicoes.get(evento);
    }

    //Visto que um evento pode não seguir de uma ação, serão implementados dois
    //métodos de transição. Neste métodos  é inserido uma entrada ao dicionário
    //de transições.
    //Para evitar redundâcia, fatoriza-se o sistema através da delegação onde a
    //ação recebida é simplemeste nula.

    public Estado transicao (Evento evento, Estado estadoSucessor, Acao acao){
        transicoes.put(evento, new Transicao(estadoSucessor,acao));
        return this;
    }
}