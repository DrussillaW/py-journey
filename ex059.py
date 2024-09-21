from colorama import Fore, Style

print(f'{"DESAFIO 59":=^40}')
print(f'{Fore.GREEN + "MENU OPÇÕES" + Style.RESET_ALL:^50}\n')

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    opcao = int(input('''\nO que deseja fazer: 
    [1] Somar
    [2] Multiplicar
    [3] Maior valor
    [4] Novos números
    [5] Sair do programa
    >>> '''))
    if opcao == 1:
        soma = num1 + num2
        print('\nA soma de {} + {} é {}.'.format(num1, num2, Fore.GREEN + str(soma) + Style.RESET_ALL))
    elif opcao == 2:
        multiplicar = num1 * num2
        print('\nA multiplicação de {} * {} é {}.'.format(num1, num2, Fore.GREEN + str(multiplicar) + Style.RESET_ALL))
    elif opcao == 3:
        if num1 > num2:
            print('\nO maior número entre {} e {} é {}.'.format(num1, num2, Fore.GREEN + str(num1) + Style.RESET_ALL))
        else:
            print('\nO maior número entre {} e {} é {}.'.format(num1, num2, Fore.GREEN + str(num2) + Style.RESET_ALL))
    elif opcao == 4:
        num1 = int(input('\nDigite um novo valor: '))
        num2 = int(input('Digite mais um valor: '))
    elif opcao not in [1, 2, 3, 4, 5]:
        print(Fore.CYAN + '\nOpção inválida. Escolha novamente!' + Style.RESET_ALL)

print(Fore.RED + '\nEncerrando o programa!' + Style.RESET_ALL)

