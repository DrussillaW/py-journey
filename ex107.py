from utils.helper import titulo
from utilidadescev import moeda

titulo('EXERCITANDO MÓDULOS', 107)

d = float(input('Digite o preço: R$'))
print(f'A metade de R${d} é R${moeda.metade(d)}')
print(f'O dobro de R${d} é R${moeda.dobrar(d)}')
print(f"Aumentando em 10%, temos R${moeda.aumentar(d, 10):.2f}")
print(f'Diminuindo em 13%, temos R${moeda.diminuir(d, 13):.2f}')
