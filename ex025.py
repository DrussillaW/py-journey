print(f'{"DESAFIO 25":=^40}')

nome = input('Digite seu nome completo: ')
up_nome = nome.upper()
# div_nome = up_nome.split()
nome_proc = 'SILVA'

if nome_proc in up_nome:
    print('Seu nome tem SILVA.')
else:
    print('Seu nome não tem SILVA.')

# nome = input('Digite seu nome completo: ').strip()
# print('Seu nome tem SILVA? {}'.format('SILVA' in nome.upper()))