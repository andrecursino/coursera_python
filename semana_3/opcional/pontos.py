from math import sqrt

ax = int(input('Coordenada x: '))
ay = int(input('Coordenada y: '))
bx = int(input('Coordenada x: '))
by = int(input('Coordenada y: '))
distanciaAB = sqrt(((ax-bx)**2) + ((ay-by)**2))
if distanciaAB >= 10:
    print('longe')
else:
    print('perto')