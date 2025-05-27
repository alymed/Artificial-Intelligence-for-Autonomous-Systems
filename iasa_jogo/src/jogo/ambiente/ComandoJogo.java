package jogo.ambiente;

import ambiente.Comando;

//ENUM --> classificador que represente um grupo de constantes
public enum ComandoJogo implements Comando {
    PROCURAR,APROXIMAR,OBSERVAR,FOTOGRAFAR;
    @Override //elimina a complexidade desorganizada
    public void mostrar(){
        System.out.printf("Ação: %s\n", this);
    }
}
