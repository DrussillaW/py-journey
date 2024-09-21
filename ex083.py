from colorama import Fore

print(f'{"DESAFIO 83":=^40}')
print(f'{Fore.GREEN}{"ANÁLISE DE EXPRESSÕES COM LISTA":^40}{Fore.RESET}')
print(f'{"="*40:^40}')


equacao = str(input('Qual expressão deseja calcular: '))
cont_fecha = []
for c in equacao:
    if c == '(':
        cont_fecha.append(')')
    elif c == ')':
        if len(cont_fecha) == 0:
            cont_fecha.append('(')
            break
        else:
            cont_fecha.pop()

if len(cont_fecha) == 0:
    print(f'A sua equação é {Fore.GREEN}VÁLIDA{Fore.RESET}. PARABÉNS!')
else:
    print(f'A sua equação {Fore.GREEN}NÃO é VÁLIDA{Fore.RESET}!')








