def MinMax(temperaturas):
    print('A menor temperatura do mês foi: {} C.'.format(
        minima(temperaturas)
    ))
    print('A maior temperatura do mês foi: {} C.'.format(
        maxima(temperaturas)
    ))


def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min


def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if minima(temp) != valor_esperado:
        print('Valor errado para o array {}.'.format(temp))
        print('Valor esperado: {}. Valor calculado {}'.format(valor_esperado, valor_calculado))


def testa_minima():
    print('iniciando testes')
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
    teste_pontual([30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 22], 22)
    teste_pontual([-15, -12, 0, 20, 30], -15)
    print('terminando teste')

MinMax([30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 26, 30, 27, 24, 25, 26, 22])