from utils.helper import titulo, pline
from colorama import Fore
titulo('VOTAÇÃO', 101)


def voto(ano):
    from datetime import datetime
    i = datetime.now().year - ano
    if i > 70 or 16 <= i < 18:
        return f'Com {i} anos: {Fore.BLUE}VOTO OPCIONAL{Fore.RESET}.'
    if i < 16:
        return f'Com {i} anos: {Fore.BLUE}NÃO VOTA{Fore.RESET}.'
    if i >= 18:
        return f'Com {i} anos: {Fore.BLUE}VOTO OBRIGATÓRIO{Fore.RESET}.'


# Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
pline()

