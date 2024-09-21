from utils.helper import titulo
from utilidadescev import moeda

titulo('FORMATANDO MOEDAS', 108)

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobrar(p))}')
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')

