from colorama import Fore

print(f'{"DESAFIO 89":=^40}')
print(f'{Fore.GREEN}{"BOLETIM":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

print(f'{Fore.GREEN}{"CADASTRO DE ALUNO":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

alunos_notas = []
aluno = []
while True:
    nome = str(input('Nome: ')).title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    alunos_notas.append(aluno[:])
    aluno.clear()
    resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while resp not in ['S', 'N']:
        resp = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'{"="*40:^40}')
print(f'{"Nº":<7}{"Nome":<7}{"Média":>25}')
print(f'{"-"*40:^40}')

for i, aluno_nota in enumerate(alunos_notas):
    media = (aluno_nota[1] + aluno_nota[2]) / 2
    print(f'{str(i+1):<7}{aluno_nota[0]:<9}{media:>23.2f}')
print(f'{"-"*40:^40}')

while True:
    mostrar = int(input(f'{Fore.GREEN}Deseja ver quais notas dos alunos{Fore.RESET} (999 para interromper): '))
    if mostrar == 999:
        print(f'{"-"*40:^40}')
        print(f'{Fore.CYAN}{"PROGRAMA ENCERRADO!":^40}{Fore.RESET}')
        break
    elif mostrar <= 0 or mostrar > len(alunos_notas):
        print(f'{Fore.RED}Aluno escolhido INVÁLIDO. Tente novamente...{Fore.RESET}')
    else:
        aluno_escolhido = alunos_notas[mostrar-1]
        print(f'As notas de {Fore.CYAN}{aluno_escolhido[0]}{Fore.RESET} foram: {Fore.CYAN}[{aluno_escolhido[1]}] [{aluno_escolhido[2]}]{Fore.RESET}')
        print(f'{"-"*40:^40}')

