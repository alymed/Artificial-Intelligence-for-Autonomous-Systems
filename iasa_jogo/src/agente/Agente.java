package agente;

import ambiente.Ambiente;
import ambiente.Evento;

//CLASSE --> constituída pelos atributos (estrutura) e pelas operações (comportamento)
public class Agente {
    private Ambiente ambiente;
    private Controlo controlo = new Controlo() {};
    //É composto pela classe Controlo e implementa Ambiente

    //AGENTE --> está presente num ambiente onde é possível
    //executar comandos e observar eventos (percepcionar).
    public Agente(Ambiente ambiente, Controlo controlo){
        this.ambiente=ambiente;
        this.controlo=controlo;
    }

    //O executar consiste no agente realizar uma ação. Desta forma, primeiro, ele
    //percepciona um evento no ambiente (método percepcionar()), gerando uma percepcao
    //A classe Controlo a processará, gerando uma ação. Com o método atuar(), esta
    //ação será acionada.
    public void executar(){
        Percepcao percepcao = percepcionar();
        Acao acao = controlo.processar(percepcao);
        atuar(acao);
    }

    //O agente percepciona eventos ao observar o ambiente e devolverá o evento.
    //Este evento será depois processado e transformado numa ação.
    protected Percepcao percepcionar(){
        Evento evento = ambiente.observar();
        return new Percepcao(evento);
    }

    //Se a ação recebida não for nula, o ambiente executa o comando correspondente à ação
    protected void atuar(Acao acao){
        if(acao!=null) ambiente.executar(acao.getComando());
    }
}
