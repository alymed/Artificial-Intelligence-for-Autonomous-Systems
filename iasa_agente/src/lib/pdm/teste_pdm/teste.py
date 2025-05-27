from pdm.teste_pdm.teste_pdm import Teste
from pdm.pdm import PDM
gama=0.5
    
delta_max=0.1

modelo_pdm=Teste()

pdm=PDM(modelo_pdm, gama, delta_max)
utilidade, politica = pdm.resolver()

print('Utilidade: ', utilidade)
print('Política: ', politica)