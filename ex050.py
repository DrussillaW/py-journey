print(f'{"DESAFIO 50":=^40}')
print(f'{"_Somatório_":^40}\n')

soma = 0
for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num

print('\n A soma dos números pares é: {}'.format(soma))