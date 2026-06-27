largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
valor_original_largura = largura
valor_original_altura = altura
if largura < 0 or altura < 0:
    print("Largura e/ou altura inválida")
else:
    while largura > 0:
        while altura > 0:
            if altura == valor_original_altura or altura == 1:
                print("#" * largura)
            else:
                espacos = " " * (largura - 2)
                print("#" + espacos + "#")
            altura = altura - 1
            if altura == 0:
                largura = 0