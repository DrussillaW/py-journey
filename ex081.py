from colorama import Fore

print(f'{"DESAFIO 81":=^40}')
print(f'{Fore.GREEN}{"EXTRAINDO OS DADOS DE UMA LISTA":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

conjunto = list()
cont5 = 0
while True:
    num = int(input('Digite um valor: '))
    conjunto.append(num)
    if num == 5:
        cont5 += 1
    resposta = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    while resposta not in ['S', 'N']:
        resposta = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        conjunto.sort(reverse=True)
        break

print(f'{"="*40:^40}')
if len(conjunto) > 1:
    print(f'Foram digitados {len(conjunto)} números.')
else:
    print(f'Foi digitado {len(conjunto)} número.')
print(f'A lista em ordem decrescente é: {conjunto}')
if cont5 >= 1:
    print(f'O valor 5 foi encontrado {cont5} vez(s).')
else:
    print('O valor 5 não foi encontrado!')




