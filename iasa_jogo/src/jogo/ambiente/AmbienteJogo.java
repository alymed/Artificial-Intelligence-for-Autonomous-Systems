package jogo.ambiente;

import ambiente.Ambiente;
import ambiente.Evento;
import ambiente.Comando;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

//Ambiente do jogo
public class AmbienteJogo implements Ambiente{
    private EventoJogo evento;
    private Map<String, EventoJogo> eventos;
    private Map<String, ComandoJogo> comandos;
    private Scanner scanner = new Scanner(System.in);

    public AmbienteJogo(){
        //Um HashMap guarda objetos em pares de "key/value". Desta forma, pode-se aceder ao
        //objeto por um outro tipo de objeto.
        eventos = new HashMap<String, EventoJogo>();
        eventos.put("s",EventoJogo.SILENCIO);
        eventos.put("r",EventoJogo.RUIDO);
        eventos.put("a",EventoJogo.ANIMAL);
        eventos.put("f",EventoJogo.FUGA);
        eventos.put("o",EventoJogo.FOTOGRAFIA);
        eventos.put("t",EventoJogo.TERMINAR);

        comandos = new HashMap<String, ComandoJogo>();
        comandos.put("p",ComandoJogo.PROCURAR);
        comandos.put("a",ComandoJogo.APROXIMAR);
        comandos.put("o",ComandoJogo.OBSERVAR);
        comandos.put("f",ComandoJogo.FOTOGRAFAR);
    }

    //A evoluação do ambiente consiste na constante geração dos eventos
    public void evoluir(){
        evento=gerarEvento();
    }
    public Evento observar(){
        evento.mostrar();
        return evento;
    }
    public void executar(Comando comando){
        comando.mostrar();
    }

    //É neste método que o utilizador introduz o evento.
    private EventoJogo gerarEvento(){
        System.out.println("\nEvento? ");
        String textoComando = scanner.next();
        return eventos.get(textoComando);
    }

    //Pelo atríbuto EventoJogo ser do tipo {read only}, será declarado como privado e
    //terá o método público getEventoJogo() como uma forma de o aceder apenas.
    public EventoJogo getEventoJogo(){
        return evento;
    }
}
