print(f'{"DESAFIO 44":=^40}')
print(f'{"Preço Final":^40}')

produto = float(input('Qual o valor do produto: '))
opcao = int(input('''Qual a forma de pagamento:
[1] Dinheiro/Cheque
[2] Cartão à vista
[3] Cartão 2x
[4] Cartão 3x
Opção escolhida: '''))
valor_pago = 0

if opcao == 1:
    valor_pago = produto - (produto * 0.1)
    print('Você recebeu um desconto de 10%.\nO valor a ser pago é R${:.2f}'.format(valor_pago))
elif opcao == 2:
    valor_pago = produto - (produto * 0.05)
    print('Está opção tem 5% de desconto.\nO preço a ser pago é de R${:.2f}'.format(valor_pago))
elif opcao == 3:
    valor_pago = produto / 2
    print('Essa opção não gera descontos. O preço cobrado é 2x de R${:.2f}'.format(valor_pago))
elif opcao == 4:
    valor_pago = (produto + (produto * 0.2)) / 3
    print('Essa opção cobrará acréscimos de 20% sobre o valor.\nO valor a ser pago é 3x de R${:.2f}'.format(valor_pago))
else:
    print('A opção escolhida não é válida.')