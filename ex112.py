from utilidadescev.dado import leiadinheiro
from utils.helper import titulo, pline
from utilidadescev.moeda import resumo

titulo('DADOS MONETÁRIOS', 112)


valor_preco = leiadinheiro('Digite o preço: R$')
resumo(valor_preco, 80, 35)

