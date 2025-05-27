package ambiente;

public interface Ambiente {

    //Ambiente geral
    //Um ambiente evolui no tempo, onde comandos podem ser executados e eventos podem ser observados.
    default void evoluir(){}

    default Evento observar(){
        return null;
    }

    default void executar(Comando comando){}
}
