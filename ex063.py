from colorama import Fore, Style

print(f'{"DESAFIO 63":=^40}')
print(f'{Fore.GREEN + "SEQUÊNCIA FIBONACCI" + Style.RESET_ALL:^50}\n')

numero = int(input('Quantos termos você quer mostra: '))
fib_1 = 0
fib_2 = 1
contador = 3

if numero == 1:
    print('{} → '.format(fib_1), end='')
elif numero == 2:
    print('{} → {} → '.format(fib_1, fib_2), end='')
elif numero >= 3:
    print('{}  → {}  → '.format(fib_1, fib_2), end='')
    while contador <= numero:
        novo_fib = fib_1 + fib_2
        print('{} → '.format(novo_fib), end='')
        fib_1 = fib_2
        fib_2 = novo_fib
        contador += 1
print(Fore.GREEN + 'FIM' + Style.RESET_ALL)


