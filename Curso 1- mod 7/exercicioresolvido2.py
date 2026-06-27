def éPrimo(n):
    divisor = 2
    while n > divisor:
        if n % divisor == 0:
            return "não primo"
        divisor = divisor + 1
    return "primo"

def fatores_primos():
    n = int(input("Digite um número inteiro maior que 1: "))
    print(éPrimo(n))
    fator = 2
    multiplicidade = 0
    while n > 1:
        while n % fator == 0:
            multiplicidade = multiplicidade + 1
            n = n / fator
        if multiplicidade > 0:
            print("fator",fator,"multiplicidade",multiplicidade)
        fator = fator + 1
        multiplicidade = 0
fatores_primos()