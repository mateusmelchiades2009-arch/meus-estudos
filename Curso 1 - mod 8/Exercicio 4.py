numero = 1
lista_do_usuario = []
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        lista_do_usuario.append(numero)
lista_do_usuario.reverse()
for n in lista_do_usuario:
    print(n)
