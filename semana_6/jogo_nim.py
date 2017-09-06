def main():
    tipo_jogo = 0
    while tipo_jogo == 0:
        #menu de opcoes
        print('Bem-vindo ao jogo do NIM! Escolha:\n'
              '\n'
              '1 - para jogar uma partida isolada')
        tipo_jogo = int(input('2 - para jogar um campeonato '))
        print('')
        if tipo_jogo == 1:
            print('Voce escolheu uma partida isolada!')
            partida()
            break
        if tipo_jogo == 2:
            print('Voce escolheu um campeonato')
            campeonato()
            break
        else:
            print('Opcao invalida\n')
            tipo_jogo = 0


def partida():
    n = int(input('Quantas pecas? '))
    m = int(input('Limite de peças por jogada? '))

    vez_do_computador = True
    if n % (m+1) == 0:
        print('Voce comeca!\n')
        vez_do_computador = False
    else:
        print('Computador comeca!\n')

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            vez_do_computador = False
            print('Computador retirou {} pecas.'.format(jogada))
        else:
            jogada = usuario_escolhe_jogada(n, m)
            vez_do_computador = True
            print('Voce retirou {} pecas.'.format(jogada))
        n = n - jogada
        print('Restam apenas {} peças no jogo.\n'.format(n))

    if vez_do_computador:
        print('Voce ganhou!')
    else:
        print('O computador ganhou!')


def computador_escolhe_jogada(n, m):
    print('Vez do computador')
    if n <= m:
        return n
    else:
        quantia = n % (m+1)
        if quantia > 0:
            return quantia
        return m


def usuario_escolhe_jogada(n, m):
    print('Sua vez!\n')
    jogada = 0
    while jogada == 0:
        jogada = int(input('Quantas pecas vai tirar? '))
        if jogada > n or jogada < 1 or jogada > m:
            print('Ooops! Jogada invalida, tente de novo.')
            jogada = 0
    return jogada


def campeonato():
    print('Voce escolheu um campeonato!\n')
    print('**** Rodada 1 ****\n')
    partida()
    print('**** Rodada 2 ****\n')
    partida()
    print('**** Rodada 3 ****\n')
    partida()
    print('**** Final do campeonato! ****\n')
    print('Placar: Voce 0 X 3 Computado')


print(main())
