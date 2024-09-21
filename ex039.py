from datetime import date

print(f'{"DESAFIO 36":=^40}')

print(f'{"_ALISTAMENTO_":^40}')

ano = int(input('\nQual seu ano de nascimento: '))
ano_alist = date.today().year - ano

if ano_alist < 18:
    print('Ainda não precisa se alistar. Deverá se alistar daqui a {}'.format(18 - ano_alist))
elif ano_alist == 18:
    print('É hora de se alistar! \U0001F4AA')
elif ano_alist > 18:
    print('O tempo de se alistar já passou {} ano(s).'.format(ano_alist - 18))