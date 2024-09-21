from datetime import date

print(f'{"DESAFIO 36":=^40}')

print(f'{"_CONFEDERAÇÃO DE NATAÇÃO_":^40}')

ano_nasc = int(input('\nDigite o ano do seu nascimento: '))
ano = date.today().year - ano_nasc

if ano <= 9:
    print('Categoria MIRIM')
elif 9 < ano <= 14:
    print('Categoria INFANTIL')
elif 14 < ano <= 19:
    print('Categoria JUNIOR')
elif 19 < ano <= 25:
    print('Categoria SÊNIOR')
elif ano > 25:
    print('Categia MASTER')