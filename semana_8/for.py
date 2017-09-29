frutas_exoticas = ['jaboticaba', 'cupuaçu', 'graviola']
for fruta in frutas_exoticas:
    print('Eu adoro {}'.format(fruta))

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

for i in range(0, 100, 3): # passo negativo tras para frente
    print(i)
pares  = range(0, 40, 2)
print()

for i in pares:
    print(i)
print()

for i in range(len(primos)):
    primos[i] = primos[i] ** 3

cubos_dos_primos = primos
print(cubos_dos_primos)