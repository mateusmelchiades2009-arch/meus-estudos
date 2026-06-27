def é_primo(n):
    if n < 2:
        return False
    divisor = 2
    while n > divisor:
        if n % divisor == 0:
            return False
        divisor = divisor + 1
    return True
def n_primos(n):
    contador = 0
    teste = 2
    while teste <= n:
        if é_primo(teste) == True:
            contador = contador + 1
        teste = teste + 1

    return contador
print(n_primos(4))
