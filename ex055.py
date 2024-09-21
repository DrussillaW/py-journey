from colorama import Fore, Style

print(f'{"DESAFIO 55":=^40}')
print(Fore.GREEN + f'{"_MAIOR OU MENOR PESO_":^40}\n' + Style.RESET_ALL)

qtd_pesos = int(input('Digite quantas pessoas vão se pesar: '))
maior_peso = 0
menor_peso = 1000

for i in range(0, qtd_pesos):
    peso = float(input('Digite seu peso atual: '))
    if maior_peso < peso:
        maior_peso = peso
    if menor_peso > peso:
        menor_peso = peso

print('O maior peso é {}'.format(Fore.GREEN + str(maior_peso) + Style.RESET_ALL))
print('O menor peso é {}'.format(Fore.GREEN + str(menor_peso) + Style.RESET_ALL))

