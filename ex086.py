from colorama import Fore

print(f'{"DESAFIO 86":=^40}')
print(f'{Fore.GREEN}{"MATRIZ":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

# matriz = [[], [], []]
# x = y = 0
# for n in range(0, 9):
#     valor = int(input(f'Digite um valor para {x, y}: '))
#     y += 1
#     if x == 0:
#         matriz[0].append(valor)
#     if x == 1:
#         matriz[1].append(valor)
#     if x == 2:
#         matriz[2].append(valor)
#     if y == 3:
#         x += 1
#         y = 0
# print(f'{"="*40:^40}')
# print(f'{Fore.GREEN}[{matriz[0][0]:^6}][{matriz[0][1]:^6}][{matriz[0][2]:^6}]{Fore.RESET}')
# print(f'{Fore.GREEN}[{matriz[1][0]:^6}][{matriz[1][1]:^6}][{matriz[1][2]:^6}]{Fore.RESET}')
# print(f'{Fore.GREEN}[{matriz[2][0]:^6}][{matriz[2][1]:^6}][{matriz[2][2]:^6}]{Fore.RESET}')

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
print(f'{"="*40:^40}')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
    print()