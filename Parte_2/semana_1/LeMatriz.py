A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        # cria linha i
        linha = []
        for j in range(num_colunas):
            valor = int(input('Digite o elemento [{}][{}]'.format(
                str(i), str(j)
            )))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def le_matriz():
    lin = int(input('Digite o numero de linhas da matriz: '))
    col = int(input('Digite o número de colunas da matriz: '))
    return cria_matriz(lin, col)

for n in le_matriz():
    print(n, end='\n')

le_matriz()