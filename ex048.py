from colorama import Fore, Style

print(f'{"DESAFIO 48":=^40}')
print(f'{"Soma de Múltiplos":^40}')

soma = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        soma += c
print('\nA soma dos múltiplos de 3 entre 1 e 500 é: {}'.format(Fore.RED + str(soma) + Style.RESET_ALL))
