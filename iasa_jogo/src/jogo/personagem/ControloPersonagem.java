package jogo.personagem;

import agente.Acao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maquest.Estado;
import maquest.MaquinaEstados;
import maquest.Transicao;

import javax.rmi.PortableRemoteObject;

//A classe ControloPersonagem tem a inteligência da personagem, controla os seus comportamentos.
//Por outras palavras, o comportamento é um sistema que evolui ao longo do tempo e consiste na forma
//como o sistema age relativamente à informação que sai e entra
public class ControloPersonagem implements Controlo {
    private MaquinaEstados maqEst; //ControloPersonagem é composta por uma maquina de estados

    public ControloPersonagem(){
        //O construtor da classe pode ser visto como uma função de transformação,
        //ou seja, uma função que perante as entradas e do estado atual do sistema
        //gera as saídas e o próximo estado.
        //FUNÇÃO DE TRANSIÇÃO DE ESTADO (delta): Q x sigma (alfabeto de entrada) --> Z (alfabeto de saída)
        //FUNÇÃO DE SAÍDA (lameda): Q x sigma (alfabeto de entrada) --> Z (alfabeto de saída)

        //Definição dos estados da personagem
        Estado procura = new Estado("Procura");
        Estado inspecao = new Estado("Inspeção");
        Estado obsecacao = new Estado("Observação");
        Estado registo = new Estado("Registo");

        //Definição das ações que a personagem pode executar
        Acao procurar = new Acao(ComandoJogo.PROCURAR);
        Acao aproximar = new Acao(ComandoJogo.APROXIMAR);
        Acao fotografar = new Acao(ComandoJogo.FOTOGRAFAR);
        Acao observar = new Acao(ComandoJogo.OBSERVAR);

        //Definição da dinâmica do comportamento da personagem
        //Nesta secção de código é utilizada uma linguagem hospedeira que simplifica a sintaxe da linguagem.

        procura
                .transicao(EventoJogo.SILENCIO,procura,procurar)
                .transicao(EventoJogo.RUIDO, inspecao,aproximar)
                .transicao(EventoJogo.ANIMAL,obsecacao,aproximar);
        inspecao
                .transicao(EventoJogo.RUIDO,inspecao,procurar)
                .transicao(EventoJogo.ANIMAL,obsecacao,aproximar)
                .transicao(EventoJogo.SILENCIO,procura,null);
        obsecacao
                .transicao(EventoJogo.FUGA,inspecao,null)
                .transicao(EventoJogo.ANIMAL,registo,observar);
        registo
                .transicao(EventoJogo.ANIMAL,registo,fotografar)
                .transicao(EventoJogo.FUGA, procura,null)
                .transicao(EventoJogo.FOTOGRAFIA,procura,null);

        maqEst=new MaquinaEstados(procura); //fonte de transição inicial da máquina de estado
    }

    //O método processar gera uma ação a partir de uma percepção recebida como parâmetro.
    //Com o evento precepcionado, processamo-lo na máquina de estado e geramos a ação.
    //Esta ação será mostrada e retornada, sendo depois posta em execução.

    public Acao processar(Percepcao percepcao){
        Evento evento = percepcao.getEvento();
        Acao acao = maqEst.processar(evento);
        mostrar();
        return acao;
    }

    //Print to estado atual da personagem
    private void mostrar(){
        System.out.printf("Estado: %s\n",getEstado().nome);
    }

    //Visto que o atributo estado é do tipo {read only}, o objeto será
    //privado e poderá ser acedido (lido) com o método público getEstado().
    //Como o ControloPersonagem é composto pela máquina de estado e está já
    //tinha acesso ao atributo estado, a relação aqui feita utiliza este
    //objeto como ponte.
    public Estado getEstado(){
        return maqEst.getEstado();
    }
}
