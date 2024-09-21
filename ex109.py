from utils.helper import titulo
from utilidadescev import moeda

titulo('FORMATANDO MOEDAS 2.0', 109)

preco = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobrar(preco, True)}')
print(f'Aumentando em 10%, temos {moeda.aumentar(preco, 10, False)}')
print(f'Diminuindo em 13%, temos {moeda.diminuir(preco, 13, True)}')
