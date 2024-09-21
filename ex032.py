from datetime import datetime

print(f'{"DESAFIO 32":=^40}')

print('\nÉ Bissexto?')

ano_in = int(input('Digite um ano ou coloca 0 para testar o ano atual: '))
if ano_in == 0:
    ano = datetime.now().year
else:
    ano = ano_in
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO.'.format(ano))

