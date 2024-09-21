print(f'{"DESAFIO 36":=^40}')

print(f'{"_TIPO DE TRIÂNGULO_":^40}')

r1 = int(input('\nDigite um valor de reta: '))
r2 = int(input('Digite outro valor de reta: '))
r3 = int(input('Digite mais um valor de reta: '))

forma_triangulo1 = r1 < r2 + r3
forma_triangulo2 = r2 < r1 + r3
forma_triangulo3 = r3 < r2 + r1

if forma_triangulo1 and forma_triangulo2 and forma_triangulo3:
    if r1 == r2 == r3:
        print('É um TRIÂNGULO EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um TRIÂNGULO ISÓSCELES.')
    else:
        print('É um TRIÂNGULO ESCALENO.')
else:
    print('Não é um TRIÂNGULO')
