from colorama import Fore

print(f'{"DESAFIO 79":=^40}')
print(f'{Fore.GREEN}{"VALORES ÚNICOS EM UMA LISTA":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print(f'{Fore.RED}Esse valor já foi adicionado!{Fore.RESET}')
    else:
        valores.append(num)
        print(f'{Fore.GREEN}Adicionado com SUCESSO.{Fore.RESET}')
    novo = ''
    while novo not in ['S', 'N']:
        novo = str(input('Deseja adicionar outro valor [S/N]: ')).upper().strip()[0]
    if novo == 'N':
        valores.sort()
        break
print(f'{"="*40:^40}')
print(f'Os valores digitados foram: {Fore.GREEN}{valores}{Fore.RESET}')