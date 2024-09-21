import unidecode

print(f'{"DESAFIO 31":=^40}')
print('Qual o valor da passagem? \U0001F914')

caminho = int(input('\nQual a distância percorrida em Km? '))
passagem = 0
if caminho <= 200:
    passagem = caminho * 0.5
    print('O valor da sua passagem será R${:.2f}'.format(passagem))
else:
    passagem = caminho * 0.45
    print('O valor da sua passagem será R${:.2f}'.format(passagem))