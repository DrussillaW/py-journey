from colorama import Fore

print(f'{"DESAFIO 77":=^40}')
print(f'{Fore.GREEN}{"ANALISANDO PALAVRAS EM TUPLAS":^40}{Fore.RESET}')
print(f'{"="*40:^40}')

palavras = ('casa', 'hotel', 'carro', 'mouse', 'bolsa', 'tartaruga', 'capacete', 'oculos', 'livro', 'cueca', 'controle')

for word in palavras:
    vogais = ''
    for c in word:
        if c in 'aeiou':
            vogais += c + ', '
    print(f'A palavra {Fore.GREEN}{word.upper()}{Fore.RESET} tem as vogais: {Fore.YELLOW}{vogais[:-2]}{Fore.RESET}.')
print(f'{"="*40:^40}')
