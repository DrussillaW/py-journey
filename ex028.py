print(f'{"DESAFIO 28":=^40}')
import random

print('Pensarei em um número entre 0 e 5...')
num_aleatorio = random.randint(0, 5)

num_usuario = int(input('Em qual número pensei? '))

if num_usuario == num_aleatorio:
    print('PARABÉNS! Você acertou.')
else:
    print('VOCÊ PERDEU! O número escolhido foi {}.'.format(num_aleatorio))