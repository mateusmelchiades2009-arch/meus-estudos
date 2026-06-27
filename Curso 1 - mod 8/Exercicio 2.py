lista = [1,2,3]
def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma
print(soma_elementos(lista))