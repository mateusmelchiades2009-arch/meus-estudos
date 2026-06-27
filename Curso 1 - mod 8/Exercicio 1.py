lista = [2, 4, 2, 2, 3, 3, 1]
def remove_repetidos(lista):
    lista_limpa = []
    for n in lista:
        if n not in lista_limpa:
            lista_limpa.append(n)
    return sorted(lista_limpa)
print(remove_repetidos(lista))
