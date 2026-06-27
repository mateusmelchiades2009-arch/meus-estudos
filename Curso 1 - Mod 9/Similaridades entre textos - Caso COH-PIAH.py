import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]
def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

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

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    i = 0
    while i < 6:
        diferenca = abs(as_a[i] - as_b[i])
        soma += diferenca
        i = i + 1
    return soma / 6

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto)
    lista_frases = []
    for s in lista_sentencas:
        lista_frases.extend(separa_frases(s))
    lista_palavras = []
    for f in lista_frases:
        lista_palavras.extend(separa_palavras(f))
    total_palavras = len(lista_palavras)
    soma_letras = 0
    for t in lista_palavras:
        soma_letras = soma_letras + len(t)
    num1 = soma_letras / total_palavras
    num2 = n_palavras_diferentes(lista_palavras) / total_palavras
    num3 = n_palavras_unicas(lista_palavras) / total_palavras
    num4 = sum(len(s) for s in lista_sentencas) / len(lista_sentencas)
    num5 = len(lista_frases) / len(lista_sentencas)
    num6 = sum(len(f) for f in lista_frases) / len(lista_frases)
    return [num1, num2, num3, num4, num5, num6]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    ass1 = calcula_assinatura(textos[0])
    menor_grau = compara_assinatura(ass1, ass_cp)
    texto_infectado = 1
    i = 1
    while i < len(textos):
        ass_texto = calcula_assinatura(textos[i])
        grau_atual = compara_assinatura(ass_texto, ass_cp)
        if grau_atual < menor_grau:
            menor_grau = grau_atual
            texto_infectado = i + 1
        i = i + 1
    return texto_infectado
ass_cp = le_assinatura()
textos = le_textos()
resultado = avalia_textos(textos, ass_cp)
print(f"O autor do texto {resultado} está infectado com COH-PIAH")