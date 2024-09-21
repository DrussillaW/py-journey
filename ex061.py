from colorama import Fore, Style

print(f'{"DESAFIO 61":=^40}')
print(f'{Fore.GREEN + "PROGRESSÃO ARITMÉTICA 2.0" + Style.RESET_ALL:^50}\n')

inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
final = (razao * 10) + inicio
contador = inicio
pa = ''
termo = inicio
cont = 1

print('\nP.A. de início {} razão {} é: '.format(Fore.CYAN + str(inicio) + Style.RESET_ALL, Fore.CYAN + str(razao) + Style.RESET_ALL), end='')


# while contador < final:
#     pa = pa + str(contador) + ', '
#     contador += razao
#
# print(pa[:-2])
# print(Fore.CYAN + '\nFIM'+ Style.RESET_ALL)

# Outro solução:

while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += razao
    cont += 1
print(Fore.CYAN + 'FIM'+ Style.RESET_ALL)

# Outro jeito de imprimir

# while contador < final:
#     print('{}'.format(contador) if contador + razao >= final else '{}, '.format(contador), end='')
#     contador += razao