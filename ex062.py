from colorama import Fore, Style

print(f'{"DESAFIO 62":=^40}')
print(f'{Fore.GREEN + "PROGRESSÃO ARITMÉTICA 3.0" + Style.RESET_ALL:^50}\n')

inicio = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = inicio
contador = 1
count = 10
print('')

while contador <= count:
    print('{} → '.format(termo), end='')
    termo += razao
    contador += 1
    if contador > count:
        print('PAUSA')
        count += int(input('\nDeseja mostrar mais quantos termos? '))
        # count = count + int(input('\nDeseja mostrar mais quantos termos? '))
print(Fore.CYAN + '\nProgressão com {} termos mostrados.'.format(count) + Style.RESET_ALL)



