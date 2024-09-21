import random

print(f'{"DESAFIO 45":=^40}')
print(f'{"JOKENPÔ":^40}')

pedra = 1
papel = 2
tesoura = 3
escolhas_possiveis = [pedra, papel, tesoura]

jogador_escolha = int(input('''\nEscolha uma opção:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Qual a sua jogada: \n'''))

if jogador_escolha in escolhas_possiveis:
    pc_escolha = random.choice(escolhas_possiveis)
    if jogador_escolha == pc_escolha:
        print('Vocês EMPATARAM! Ambos escolheram a mesma opção de {}'.format(escolhas_possiveis))
    elif jogador_escolha == pedra:
        if pc_escolha == papel:
            print('Você PERDEU. O PC escolheu PAPEL!')
        else:
            print('Você GANHOU. O PC escolheu TESOURA!')
    elif jogador_escolha == papel:
        if pc_escolha == tesoura:
            print('Você PERDEU. O PC escolheu TESOURA!')
        else:
            print('Você GANHOU. O PC escolheu PEDRA!')
    elif jogador_escolha == tesoura:
        if pc_escolha == pedra:
            print('Você PERDEU. O PC escolheu PEDRA!')
        else:
            print('Você GANHOU. O PC escolheu PAPEL!')
else:
    print('Você não fez uma escolha válida.')

