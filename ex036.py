print(f'{"DESAFIO 36":=^40}')

print(f'\n{"EMPRÉSTIMO BANCÁRIO":^40}')

casa = float(input('Qual o valor do imóvel: '))
salario = float(input('Qual seu salário atual: '))
ano = int(input('Em quantos anos pretende pagar: '))
meses = ano * 12
parcela = casa / meses

if parcela <= salario * 0.30:
    print('Seu crédito foi APROVADO. O valor da prestação ficará em {:.2f}'.format(parcela))
else:
    print('Seu empréstimo foi NEGADO.\nO valor da parcela execedeu 30% do seu salário.\nO valor ficou em {:.2f}'
          '\nA parcela ideal não pode ulprassar {:.2f}'.format(parcela, (salario * 0.30)))