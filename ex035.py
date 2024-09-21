print(f'{"DESAFIO 35":=^40}')
print(f'{"É um TRIÂNGULO?":^40}')

r1 = int(input('Digite um valor de reta: '))
r2 = int(input('Digite outro valor de reta: '))
r3 = int(input('Digite mais um valor de reta: '))

# forma_triangulo1 = r1 < r2 + r3
# forma_triangulo2 = r2 < r1 + r3
# forma_triangulo3 = r3 < r2 + r1
#
# if forma_triangulo1 and forma_triangulo2 and forma_triangulo3:
#     print('É UM TRIÂNGULO')
# else:
#     print('Não é um TRIÂNGULO')

maior = r1
menor1 = r2
menor2 = r3

if r2 > r1 and r2 > r3:
    maior = r2
    menor1 = r3
    menor2 = r1
if r3 > r1 and r3 > r2:
    maior = r3
    menor1 = r2
    menor2 = r1

if maior < menor1 + menor2:
    print('Esses segmentos formam um TRIÂNGULO')
else:
    print('Esses segmentos não formam um TRIÂNGULO')
