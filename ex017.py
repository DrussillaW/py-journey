import math
from math import sqrt, hypot

print('{:=^50}'.format('VAMOS ACHAR A HIPOTENUSA?'))
print('Pensando em um triângulo retângulo, responda: ')

num1 = float(input('Comprimento do cateto oposto: '))
num2 = float(input('Comprimento do cateto adjacente: '))

cat_op = num1 ** 2
cat_ad = num2 ** 2
hip = sqrt(cat_op + cat_ad)
hip2 = math.hypot(num1, num2)

print('O valor da hipotenusa é igual a {:.2f}'.format(hip))
print('O valor da hipotenusa é igual a {:.2f}'.format(hip2))
