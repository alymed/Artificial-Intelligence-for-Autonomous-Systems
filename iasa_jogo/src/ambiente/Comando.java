package ambiente;

public interface Comando {
    //É possível mostrar os comandos executados num ambiente
    default void mostrar(){}
}
