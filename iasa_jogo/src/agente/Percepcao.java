package agente;

import ambiente.Evento;

public class Percepcao {
    //A classe Percepcao é responsável pelo evento que o agente percepciona no ambiente
    private Evento evento; //A classe Percepcao está associada à classe Evento
    public Percepcao(Evento evento){
        this.evento=evento;
    }
    //Pelo atríbuto evento ser do tipo {read only}, será declarado como privado e
    //terá o método público getEvento() como uma forma de o aceder apenas.
    public Evento getEvento(){
        return evento;
    }
}
