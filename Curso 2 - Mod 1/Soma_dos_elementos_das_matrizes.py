def soma_matrizes(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

    matriz_soma = []

    num_linhas = len(m1)
    num_colunas = len(m1[0])

    for i in range(num_linhas):
        linha_atual = []
        for j in range(num_colunas):
            soma_dos_elementos = m1[i][j] + m2[i][j]
            linha_atual.append(soma_dos_elementos)

        matriz_soma.append(linha_atual)

    return matriz_soma