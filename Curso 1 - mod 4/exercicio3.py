número = int(input("Digite um número inteiro: "))
soma = 0

while número > 0:
    digito = número % 10
    soma = soma + digito
    número = número // 10
print(soma)