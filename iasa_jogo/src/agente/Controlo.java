package agente;

//INTERFACE --> pode ser definida como um contrato que presta serviços
// independente da implementação. É um classificador que define um conjunto
// coeso de características visíveis de uma classe. Tem como um dos
// objetivos reduzir a complexidade e organizar o sistema. Uma classe
// realizará as características de uma interface ao implementa-las.
public interface Controlo {
    //A interface Controlo faz parte da classe Agente. Controlo está contida na classe Agente.
    //Verificando o nível de acopolamento, ou seja, o grau de dependência entre as partes,
    //verifica-se que a relação é forte.
    default Acao processar (Percepcao percepcao){
        return null;
    }
}
