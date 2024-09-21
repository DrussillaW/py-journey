import time
import emoji

print(f'{"DESAFIO 46":=^40}')
print(f'{"Contagem Regressiva":^40}')

festa = str(input('O que estamos comemorando? '))
print('Vamos à contagem regressiva...')
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print(emoji.emojize('BUM! BUM! POOOW!:fireworks::sparkler: FELIZ {}'.format(festa.upper())))