num = int(input('Digite um numero inteiro: '))
a = 1
rodada = 0
while num >= a:
    if num % a == 0:
        rodada = rodada + 1
    a = a + 1
if rodada == 2:
    print('primo')
else:
    print('não primo')

