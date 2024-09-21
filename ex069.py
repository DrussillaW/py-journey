from colorama import Fore, Style

print(f'{"DESAFIO 69":=^40}')
print(f'{Fore.GREEN + "CADASTRO DE PESSOAS" + Style.RESET_ALL:^50}')
print(f'{"="*40:^40}\n')

cont_sexo_mas = 0
cont_maioridade = 0
cont_mulher_menor = 0


while True:
    continuar = ''
    sexo = ''
    idade = int(input('Idade: '))
    while sexo not in ['F', 'M']:
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    if sexo == 'M':
        cont_sexo_mas += 1
    if idade > 18:
        cont_maioridade += 1
    if idade < 20 and sexo == 'F':
        cont_mulher_menor += 1
    print('~'*40)
    while continuar not in ['S', 'N']:
        continuar = str(input(Fore.RED + 'Quer continuar [S/N]: ' + Style.RESET_ALL)).upper().strip()[0]
    print('~'*40)
    if continuar == 'N':
        break
print(f'Existem {cont_maioridade} pessoas maiores de 18 anos.')
print(f'Ao todo são {cont_sexo_mas} homens registrados.')
print(f'E temos {cont_mulher_menor} mulheres com menos de 20 anos.')


