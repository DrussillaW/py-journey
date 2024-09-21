print(f'{"DESAFIO 24":=^40}')

cidade = input('Digite o nome da sua cidade: ').strip()

# big_cidade = cidade.upper()
# div_cidade = big_cidade.split()
#
# e_santo = div_cidade[0] == 'SANTO'
#
# if e_santo:
#     print('A sua cidade começa com SANTO. Congratulations')
# else:
#     print('A sua cidade não começa com SANTO.')

print(cidade[:5].upper() == 'SANTO')
