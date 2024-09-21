print('Lets Paint')
print('Qual o tamanho da sua parede?')
l = float(input('Largura: ').replace(',', '.'))
a = float(input('Altura: ').replace(',', '.'))

area = l * a
tinta = area / 2

print('Sua parede tem {:.2f}m² e será necessário {:.1f}L de tinta.'.format(area, tinta))
