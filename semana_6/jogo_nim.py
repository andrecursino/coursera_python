def campeonato():
    print('Bem-vindo ao jogo do NIM! Escolha:\n')
    print('1 - para jogar uma partida isolada')
    escolha = int(input('2 - para jogar um campeonato'))
    if escolha == 1:
        print('Você escolheu jogar uma partida isolada!')
        partida()
    else:
        print('Você escolheu um campeonato!\n')
        print('**** Rodada 1 ****\n')
        partida()
        print('**** Rodada 2 ****\n')
        partida()
        print('**** Rodada 3 ****\n')
        partida()
        print('**** Final do campeonato! ****\n')
        print('Placar: Você 0 X 3 Computado')


def partida():
    n = int(input('Quantas pecas? '))
    m = int(input('Limite de pecas por jogada? '))
    print('')
    if n % (m + 1) == 0:
        print('Voce comeca!\n')
        return usuario_escolhe_jogada(n, m)
    else:
        print('Computador comeca!\n')
        return computador_escolhe_jogada(n, m)


def computador_escolhe_jogada(n, m):
    a = 1
    b = True
    peca_robo = 0
    while a <= m and b == True:
        if n % (m + 1) == 0:
            b = False
        else:
            peca_robo = peca_robo + 1
            a = a + 1
            n = n - 1
    print('O computador tirou {} pecas.'.format(peca_robo))
    if n <= 0:
        print('Fim do jogo! O computador ganhou!\n')
    else:
        print('Agora restam {} pecas.\n'.format(n))
        peca_jogador = int(input('Quantas pecas voce vai tirar? '))
        if peca_jogador > m:
            print('Oops! Jogada invalida! Tente de novo.\n')
            return computador_escolhe_jogada(n, m)
        else:
            print('Voce tirou {} pecas.'.format(peca_jogador))
            n = n - peca_jogador  # pecas restantes
            if n < 0:
                print('Fim de jogo! Voce ganhou!')
            else:
                return computador_escolhe_jogada(n, m)



def usuario_escolhe_jogada(n, m):
    peca_jogador = int(input('Quantas pecas voce vai tirar? '))
    if peca_jogador > m:
        print('Oops! Jogada invalida! Tente de novo.\n')
        return usuario_escolhe_jogada(m, n)
    else:
        print('Voce tirou {} pecas.'.format(peca_jogador))
        n = n - peca_jogador #pecas restantes
        if n <= 0:
            print('Fim do jogo! Voce ganhou!')
        else:
            print('Agora resta apenas {} pecas '.format(n))
            a = 1
            b = True
            peca_robo = 0
            while a <= m and b == True:
                if n % (m + 1) == 0:
                    b = False
                else:
                    peca_robo = peca_robo + 1
                    a = a + 1
                    n = n - 1
            print('O computador tirou {} pecas.'.format(peca_robo))
            if n > 0:
                print('Agora restam {} pecas.\n'.format(n))
                return usuario_escolhe_jogada(n, m)
            else:
                print('Fim do jogo! O computador ganhou!\n')




print(campeonato())