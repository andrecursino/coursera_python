frase = str(input('Digite um numero inteiro: '))
tamanho = len(frase)
a = 0
b = a - 1
adj = False
while tamanho > (a + 1):
    if frase[a] == frase[a+1]:
        a = a + 1
        adj = True
    else:
        a = a + 1

if adj == True:
    print('sim')
else:
    print('nao')