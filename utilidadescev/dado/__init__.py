def leiadinheiro(msg):
    from colorama import Fore
    escrita = False
    num = 0
    while not escrita:
        mensagem = str(input(msg)).replace(',', '.')
        if mensagem.replace('.', '').isnumeric():
            num = float(mensagem)
            escrita = True
        else:
            print(f'{Fore.RED}ERRO. "{mensagem}" é um preço inválido!{Fore.RESET}')
    return num


def leiaint(msg):
    from colorama import Fore
    valido = False
    while not valido:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print(f'{Fore.RED}ERRO. Digite um número inteiro válido.{Fore.RESET}')
        except KeyboardInterrupt:
            print(f'{Fore.BLUE}\nO usuário preferiu não informar esse número.{Fore.RESET}')
            n1 = 0
            return f'{Fore.GREEN}{n1}{Fore.RESET}'
        else:
            if valido:
                int(n1)
            return f'{Fore.GREEN}{n1}{Fore.RESET}'


def leiafloat(msg):
    from colorama import Fore
    valido = False
    while not valido:
        try:
            n1 = float(input(msg))
        except (ValueError, TypeError):
            print(f'{Fore.RED}ERRO. Digite um número real válido.{Fore.RESET}')
        except KeyboardInterrupt:
            n1 = 0
            print(f'{Fore.BLUE}\nO usuário preferiu não informar esse número.{Fore.RESET}')
            return f'{Fore.GREEN}{n1}{Fore.RESET}'
        else:
            if valido:
                float(n1)
            return f'{Fore.RED}{n1}{Fore.RESET}'
