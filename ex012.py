print('{:=^50}'.format('QUAL DESCONTO?'))

produto = float(input('Qual o valor do seu produto? '))

novo_valor = produto - (produto * 0.05)

print('Seu produto com o desconto de 5% é de R$ {:.2f}'.format(novo_valor).replace('.', ','))