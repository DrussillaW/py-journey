from colorama import Fore, Style

print(f'{"DESAFIO 60":=^40}')
print(f'{Fore.GREEN + "CÁLCULO DO FATORIAL" + Style.RESET_ALL:^50}\n')

num = int(input('Qual o número quer fatorar: '))
fatorial_num = num
calculo = str(num) + ' * '

while num > 1:
    fatorial_num = fatorial_num * (num - 1)
    num -= 1
    if num == 1:
        calculo = calculo + str(num) + ' = '
    else:
        calculo = calculo + str(num) + ' * '

print('\n' + calculo + str(Fore.GREEN + str(fatorial_num) + Style.RESET_ALL))

# Outra forma de executar o mesmo Desafio:
#
# numero = int(input('Qual número quer fatorar: '))
# fatorial = 1    # recebe 1 por ser usado em multiplicação.
#
# print('Calculando: Fatorial de {}! = '.format(numero), end='')
#
# while numero > 0:
#     print('{}'.format(numero), end='')
#     print(' x ' if numero > 1 else ' = ', end='')
#     fatorial *= numero
#     numero -= 1
#
# print(fatorial)

