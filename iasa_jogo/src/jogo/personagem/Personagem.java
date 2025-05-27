package jogo.personagem;

import agente.Agente;
import agente.Controlo;
import jogo.ambiente.AmbienteJogo;

public class Personagem extends Agente {
    //A classe Personagem é extendida pela classe Agente, o que quer dizer que a
    //classe Personagem é uma especificação da classe Agente.

    //Para construir esta personagem é necessário ter em conta o ambiente onde ela
    //estará e o seu controlo, ou seja, a forma como interpretará eventos e outros.
    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem() {});
    }
}
