from utils.helper import titulo, pline
from utilidadescev.moeda import resumo

titulo('FORMATANDO MOEDAS 3.0', 110)

gasto = float(input('Digite o preço: R$'))
resumo(gasto, 80, 35)
