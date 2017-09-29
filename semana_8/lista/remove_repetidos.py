def remove_repetidos(lista):
    i = 0
    j = 1
    lista2 = []
    while i < len(lista):
        while j < len(lista):
            if lista[i] == lista[j]:
                lista2.append(j)
                del lista[j]
            j = j + 1
        i = i + 1
        j = i + 1
        lista2 = sorted(lista)
    return lista2
