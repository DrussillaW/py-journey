import math
from math import trunc
print('{:=^50}'.format('QUAL SUA PARTE INTEIRA?'))

num = float(input('Digite um número real: '))

print('A parte inteira do número {} é igual a {}'.format(num, trunc(num)))
#print('A parte inteira do número {} é igual a {}'.format(num, int(num)))