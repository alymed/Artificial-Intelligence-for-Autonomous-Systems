package jogo.ambiente;

import ambiente.Evento;

public enum EventoJogo implements Evento {
    SILENCIO,RUIDO,ANIMAL,FUGA,FOTOGRAFIA,TERMINAR;
    @Override //elimina a complexidade desorganizada
    public void mostrar(){
        System.out.printf("Evento: %s\n", this);
    }
}
