import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.\n")

    wal = float(input("Informe o tamanho medio de palavra: "))
    ttr = float(input("Informe a relação Type-Token: "))
    hlr = float(input("Informe a Razão Hapax Legomana: "))
    sal = float(input("Informe o tamanho médio de sentença: "))
    sac = float(input("Informe a complexidade média da sentença: "))
    pal = float(input("Informe o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) + " (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair): ")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    frases = re.split(r'[,:;]+', sentenca)
    return frases


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    numero_sentencas = len(sentencas)
    lista_palavras = []
    numero_frases = 0
    numero_palavras = 0
    soma_caracteres = 0
    for x in range(len(sentencas)):
        lista_frases = sentencas[x]
        soma_caracteres += len(lista_frases)
        frases = separa_frases(sentencas[x])
        numero_frases += len(frases)
        for y in range(len(frases)):
            palavras = separa_palavras(frases[y])
            for z in range(len(palavras)):
                lista_palavras.append(palavras[z])
            numero_palavras += len(palavras)
    palavras_unicas = n_palavras_unicas(lista_palavras)
    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    wal = soma_caracteres / numero_palavras
    ttr = palavras_diferentes / numero_palavras
    hlr = palavras_unicas / numero_palavras
    sal = soma_caracteres / numero_sentencas
    sac = numero_frases / numero_sentencas
    pal = soma_caracteres / numero_frases
    return [wal, ttr, hlr, sal, sac, pal]


def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somatoria = 0
    for x in range(len(as_a)):
        i = (as_b[x] - as_a[x])
        if i < 0:
            i = i * -1
        somatoria += i
    s = somatoria / 6
    return s


def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    s = compara_assinatura(ass_cp, calcula_assinatura(textos[0]))
    limite = s
    for x in range(len(textos)):
        s = compara_assinatura(ass_cp, calcula_assinatura(textos[x]))
        if s <= limite:
            cohpiah = x + 1
    return cohpiah


'''
texto1 = 'Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.'
texto2 = 'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.'
texto3 = 'NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.'
textos = [texto1, texto2, texto3]
'''

ass_cp = le_assinatura()
textos = le_textos()
print('\nO autor do texto {} está infectado com COH-PIAH'.format(avalia_textos(textos, ass_cp)))
