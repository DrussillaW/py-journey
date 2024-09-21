print(f'{"DESAFIO 52":=^40}')
print(f'{"_Número PRIMO ou NÃO_":^40}\n')

num = int(input('Digite um número: '))

if num == 0 or num == 1:
    print('Não é um número PRIMO.')
else:
    n_divisores = 0
    for c in range(1, num+1):
        if num % c == 0:
            n_divisores += 1

    if n_divisores == 2:
        print('O número {} é PRIMO!'.format(num))
    else:
        print('O número {} é COMPOSTO.'.format(num))
