print(f'{"DESAFIO 36":=^40}')

print(f'\n{"_COMPARANDO NÚMEROS_":^40}')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 < n2:
    print('O número {} é o maior valor.'.format(n2))
elif n1 > n2:
    print('O número {} é o maior.'.format(n1))
else:
    print('Não existe um número maior. Os dois números são iguais.')
