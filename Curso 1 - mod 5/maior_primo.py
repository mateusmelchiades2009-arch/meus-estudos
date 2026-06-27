def éPrimo(k):
    divisor = 2
    while k > divisor:
        if k % divisor == 0:
            return "não primo"
        divisor = divisor + 1
    return "primo"

def maior_primo(n):
    numero = n
    while numero >= 2:
        if éPrimo(numero) == "primo":
            return numero
        else:
            numero = numero - 1


