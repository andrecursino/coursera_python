flores = ['margarida', 'rosa', 'tulipa', 'cravo']
tam = len(flores) - 1
while tam >= 0:
    print(flores[tam], end=', ')
    tam = tam - 1

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone

lista1 = ['vermelho', 'verde', 'azul']

lista2 = lista1[:] #clonar

print('rosa' in lista1)
