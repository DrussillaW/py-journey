from colorama import Style, Fore

print(f'{"DESAFIO 49":=^40}')
print(f'{"TABUADA 2.0":^40}')

num = int(input('\nDigite um valor: '))
print('\nA tabuada do número {} é: '.format(Fore.GREEN + str(num) + Style.RESET_ALL))

for c in range(0, 11):
    n = num * c
    print(str(num) + ' x ' + str(c) + ' = ' + Fore.RED + str(n) + Style.RESET_ALL)