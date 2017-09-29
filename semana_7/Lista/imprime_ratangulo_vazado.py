largura = int(input('digite a altura: '))
altura = int(input('digite a largura: '))
l = 1
c = 1
while l <= altura:
    print( '#', end='')
    while c < largura-1:
        if l == 1 or l == altura:
            print('#', end='')
        else:
            print(' ', end='')
        c = c + 1

    print('#', end='')

    print('')
    l = l + 1
    c = 1