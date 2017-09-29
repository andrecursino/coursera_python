l = int(input('digite a largura: '))
h = int(input('digite a altura: '))
a = 0
b = 0

while a < h:
    while b < l:
        print('#',end='')
        b = b + 1
    print()
    a = a + 1
    b = 0
