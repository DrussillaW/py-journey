print(f'{"DESAFIO 43":=^40}')
print(f'{"Calculando IMC":^40}')

peso = float(input('Digite seu peso(Kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu IMC é {:.2f}\nVocê está ABAIXO do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é {:.2f}\nVocê está no peso IDEAL.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é {:.2f}\nVocê está com SOBREPESO.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é {:.2f}\nVocê está com OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.2f}\nVocê  está com OBESIDADE MÓRBIDA.'.format(imc))