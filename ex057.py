from colorama import Fore, Style

print(f'{"DESAFIO 57":=^40}')
print(f'{Fore.GREEN + "VALIDAÇÃO DE DADOS" + Style.RESET_ALL:^50}\n')

sexo1 = 'F'
sexo2 = 'M'
sexo = ''
while sexo1 != sexo and sexo2 != sexo:
    sexo = str(input("Informe seu sexo: [F/M] ")).strip().upper()[0]

print(Fore.GREEN + '\nSexo {} registrado com sucesso!'.format(sexo) + Style.RESET_ALL)

# sexo = str(input('Informe seu sexo: [F/M] ')).upper().strip()[0]
# while sexo not in 'FM':
#     sexo = str(input('Opção inválida. Informe seu sexo: [F/M] '))
# print('Sexo {} registrado com sucesso!'.format(sexo))

