from problema_deposito import ProblemaDeposito
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif

VOLUME_INICIAL=0
VOLUME_FINAL=9

problema =ProblemaDeposito(VOLUME_INICIAL, VOLUME_FINAL)
mec_proc = ProcuraCustoUnif()
solucao  = mec_proc.procurar(problema)
print(solucao)


# SOLUÇÃO:[Encher(2),Encher(2),Encher(2),Encher(2)]
# Dimensão:3
# Custo:21