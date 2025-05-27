from mod_prob.problema_contagem import ProblemaContagem

from pee.larg.procura_largura import ProcuraLargura
from pee.melhor_prim.aval.heuristica_contagem import HeuristicaContagem
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.prof.procura_profundidade import ProcuraProfundidade

VALOR_INCIAL = 0
VALOR_FINAL = 9
INCREMENTOS = [1,2]

problema = ProblemaContagem(VALOR_INCIAL, VALOR_FINAL, INCREMENTOS)
heuristica = HeuristicaContagem(VALOR_FINAL)

# mec_proc = ProcuraCustoUnif()
# mec_proc = ProcuraLargura()
mec_proc = ProcuraProfundidade()
# mec_proc = ProcuraAA()
# mec_proc = ProcuraSofrega()

solucao  = mec_proc.procurar(problema)
# solucao  = mec_proc.procurar(problema, heuristica)

print('Solução: ', solucao, "\nTipo: ", type(solucao), "\nDimensão: ", (solucao.dimensao))
if solucao:
    for passo in solucao:
        print('Estado passo: ',passo.estado.get_valor, '\nIncremento: ', passo.operador.get_incremento)
    print()
    passos = [passo.operador.get_incremento for passo in solucao]
    print('Passos: ', passos)

print("Dimensão: ", solucao.dimensao)
print("Custo: ", solucao.custo)