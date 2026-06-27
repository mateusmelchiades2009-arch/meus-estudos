def é_hipotenusa(h):
    i = 1
    j = 1
    while i < h:
        while j < h:
            if i**2 + j**2 == h**2:
                return True
            j = j + 1
        i = i + 1
        j = 1
    return False

def soma_hipotenusas(n):
    soma = 0
    inicio = 1
    while inicio <= n:
        if é_hipotenusa(inicio) == True:
            soma = soma + inicio
        inicio = inicio + 1
    return soma
print(soma_hipotenusas(25))