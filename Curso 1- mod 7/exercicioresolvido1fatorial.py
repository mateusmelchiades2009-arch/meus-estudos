# n = int(input("Digite um número inteiro positivo: "))
# while n >= 0:
#     fatorial = 1
#     while n > 1:
#         fatorial = fatorial * n
#         n = n - 1
#     print(fatorial)
#     n = int(input("Digite um número: "))

def fatorial_externo():
    n = int(input("Digite um número inteiro positivo: "))
    return n
def fatorial_interno():
    n = fatorial_externo()
    while n >= 0:
        fatorial = 1
        while n > 1:
            fatorial = fatorial * n
            n = n - 1
        print(fatorial)
        n = int(input("Digite um número: "))
fatorial_interno()