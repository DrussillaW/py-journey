from utils.helper import titulo, pline

titulo('CALCULANDO ÁREA', 96)


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg:.1f}m x {comp:.1f}m é de {a:.1f}m')


# Programa principal
print(f'{"Calculando área":^40}')
pline()

l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)







