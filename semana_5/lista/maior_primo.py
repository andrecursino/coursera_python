def maior_primo(k):
    a = 1
    b = 1
    c = 1
    primo = 1
    rodada = 0
    while k >= a:
        while a >= b:
            if a % c == 0:
                rodada = rodada + 1
            b = b + 1
            c = c + 1
        if rodada == 2:
            primo = a
        a = a + 1
        b = 1
        c = 1
        rodada = 0
    return primo




