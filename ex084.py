from colorama import Fore

print(f'{"DESAFIO 84":=^40}')
print(f'{Fore.GREEN}{"ANÁLISE DE DADOS COM LISTA COMPOSTA":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

# cadastro = list()
# dados = list()
#
# while True:
#     dados.append(str(input('Nome: ')).title())
#     dados.append(float(input('Peso: ')))
#     cadastro.append(dados[:])
#     dados.clear()
#     resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
#     while resp not in ['S', 'N']:
#         resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
#     if resp == 'N':
#         break
#
# pesadao = list()
# leve = list()
# maior_peso = 0
# menor_peso = 1000
# for p in cadastro:
#     if p[1] > maior_peso:
#         pesadao.clear()
#         maior_peso = p[1]
#         pesadao.append(p[0])
#     elif p[1] == maior_peso:
#         pesadao.append(p[0])
#
#     if p[1] < menor_peso:
#         leve.clear()
#         menor_peso = p[1]
#         leve.append(p[0])
#     elif p[1] == menor_peso:
#         leve.append(p[0])
#
# print(f'{"="*40:^40}')
# print(f'Ao todo foram cadastradas {len(cadastro)} pessoas.')
# print(f'O maior peso cadastrado foi {maior_peso}. Peso de {pesadao}')
# print(f'O menor peso cadastrado foi {menor_peso}. Peso de {leve}')

temporario = list()
principal = list()
maior = menor = 0

while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resp = str(input('Quer continuar [S/N]: '))
    if resp in 'Nn':
        break

print('='*40)
print(f'Ao todo foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso cadastrado foi {maior}. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso cadastrado foi {menor}. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
