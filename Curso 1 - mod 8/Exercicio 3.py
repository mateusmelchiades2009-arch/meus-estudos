lista = [1,2,10,5,-20]
def maior_elemento(lista):
    lista_limpa = []
    for inteiro in lista:
        if inteiro not in lista_limpa:
            lista_limpa.append(inteiro)
    lista_ordenada = sorted(lista_limpa)
    return lista_ordenada[-1]
print(maior_elemento(lista))