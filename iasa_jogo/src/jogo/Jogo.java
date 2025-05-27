package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

public class Jogo {
    //A classe Jogo é o cerébro de toda a estrutura construída. É onde as peças que já foram
    //montadas anteriormente seram conectadas e daram origem ao jogo pretendido.
    private static AmbienteJogo ambiente;
    private static Personagem personagem;

    //Os atributos ambiente e personagem são estáticos, o que significa que uma vez atribuido
    //valores, já não podem ser modificados.

    //Este método descreve a evolução do jogo.
    //Enquanto o evento do jogo for diferente de terminar, o ambiente continuará a
    //evoluir e a personagem a executar ações.

    private static void executar() {
        do {
            ambiente.evoluir();
            personagem.executar();
        } while (ambiente.getEventoJogo() != EventoJogo.TERMINAR);
    }

    public static void main(String[] args) {
        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);
        executar();
    }
}