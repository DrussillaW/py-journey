from colorama import Fore

print(f'{"DESAFIO 80":=^40}')
print(f'{Fore.GREEN}{"LISTA ORDENADA SEM REPETIÇÕES":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

numeros = list()

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num >= numeros[len(numeros) - 1]:
        numeros.append(num)
        print(f'{Fore.GREEN}O número {num} foi adicionado ao final da lista.{Fore.RESET}')
    else:
        for p, n in enumerate(numeros):
            if n > num:
                numeros.insert(p, num)
                print(f'{Fore.GREEN}O número {num} foi adicionado na {p + 1}ª posição.{Fore.RESET}')
                break

# for i in range(0, 5):
#     num = int(input('Digite um valor: '))
#     numeros.append(num)
#     numeros.sort()
#     posicao = numeros.index(num)
#     if posicao == (len(numeros) - 1):
#         print(f'{Fore.GREEN}O número {num} foi adicionado ao final da lista...{Fore.RESET}')
#     else:
#         print(f'{Fore.GREEN}O número {num} foi adicionado na {numeros.index(num) + 1}ª posição.{Fore.RESET}')
print(f'{"="*40:^40}')
print(f'Os valores digitados na ordem crescente foram: {Fore.GREEN}{numeros}{Fore.RESET}')
