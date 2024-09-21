import math

print(f'{"DESAFIO 36":=^40}')

print(f'{"_APROVADO OU REPROVADO_":^40}')

nota1 = float(input('\nQual a primeira nota: '))
nota2 = float(input('Qual a segunda nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('Você está REPROVADO! Sua média foi {:.1f} \u2639'.format(media))
elif 5 <= media < 7:
    print('Você está de RECUPERAÇÃO. Sua média foi {:.1f} \U0001F4DA'.format(media))
elif media >= 7:
    print('Você está APROVADO! Sua média foi {:.1f} ! Parabéns \U0001F389'.format(media))