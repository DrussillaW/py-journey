from colorama import Fore, Style

print(f'{"DESAFIO 66":=^40}')
print(f'{Fore.GREEN + "MANIPULANDO NÚMEROS" + Style.RESET_ALL:^50}\n')

num = cont = soma = 0
while True:
    print(Style.BRIGHT + '[999 para PARAR] ' + Style.RESET_ALL, end='')
    num = int(input('Digite um valor → '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'\nFoi digitado {Fore.RED}{cont}{Fore.RESET} números e a soma entre eles é {Fore.RED}{soma}{Fore.RESET}')