from colorama import Fore

print(f'{"DESAFIO 94":=^40}')
print(f'{Fore.GREEN}{"UNINDO LISTAS E DICIONÁRIOS":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

cadastro = list()
pessoa = dict()
soma_idade = 0

while True:
    pessoa['Nome'] = str.title(input('Nome: '))
    pessoa['Sexo'] = str.upper(input('Sexo [F/M]: '))[0]
    pessoa['Idade'] = int(input('Idade: '))
    cadastro.append(pessoa.copy())
    soma_idade += pessoa['Idade']
    resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    while resp not in ['S', 'N']:
        resp = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'{"="*40:^40}')
print(f'O grupo tem {Fore.BLUE}[{len(cadastro)}]{Fore.RESET} pessoas.')
print(f'A média das idades é {Fore.BLUE}{soma_idade / len(cadastro):.1f}{Fore.RESET}')

print(f'As mulheres cadastradas foram: ', end='')
for pessoa in cadastro:
    if pessoa['Sexo'] == 'F':
        print(f'{Fore.BLUE}[{pessoa["Nome"]}]{Fore.RESET} ', end='')
print()

print(f'{"="*40:^40}')
print(f'{Fore.BLUE}As pessoas com idade acima da média são:{Fore.RESET} ')
for pessoa in cadastro:
    if pessoa['Idade'] > (soma_idade / len(cadastro)):
        print(f'Nome: {pessoa["Nome"]} | Sexo: {pessoa["Sexo"]} | Idade: {pessoa["Idade"]}')


