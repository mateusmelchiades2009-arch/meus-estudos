def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    escolha = 0
    while escolha != 1 and escolha != 2:
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato")
        escolha = int(input(""))
        if escolha == 1:
            print("Voce escolheu uma partida isolada!")
            partida()
        elif escolha == 2:
            print("Voce escolheu um campeonato!")
            campeonato()
        else:
            print("Opção inválida! Tente novamente.")
    return escolha

def computador_escolhe_jogada(n, m):
    pecas_retiradas = 1
    while pecas_retiradas <= m:
        if (n - pecas_retiradas) % (m + 1) == 0:
            return pecas_retiradas
        else:
            pecas_retiradas = pecas_retiradas + 1
    return m

def usuario_escolhe_jogada(n, m):
    jogada_valida = False
    while not jogada_valida:
        jogada = int(input("Quantas peças você vai tirar? "))
        if jogada <= m and jogada > 0 and jogada <= n:
            jogada_valida = True
        else:
            print("Oops! Jogada inválida! Tente de novo.")
            jogada_valida = False
    return jogada

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    vez_do_computador = False
    if n % (m + 1) == 0:
        print("Você começa!")
        vez_do_computador = False
    else:
        print("Computador começa!")
        vez_do_computador = True
    while n > 0:
        if vez_do_computador == True:
            jogada = computador_escolhe_jogada(n, m)
            if jogada == 1:
                print("O computador tirou uma peça")
            else:
                print("O computador tirou",jogada,"peças.")

            n = n - jogada
            vez_do_computador = False

        else:
            jogada = usuario_escolhe_jogada(n, m)
            if jogada == 1:
                print("Você tirou uma peça")
            else:
                print("Você tirou",jogada,"peças.")

            n = n - jogada
            vez_do_computador = True
        if n > 0:
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")
            else:
                print("Agora restam",n," peças no tabuleiro.")

            # 4. Fim da partida (Como o computador nunca perde na estratégia, ele sempre ganha)
    print("Fim do jogo! O computador ganhou!")
    return "computador"

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    rodada = 1

    while rodada <= 3:
        print("*** Rodada",rodada,"***")
        vencedor = partida()
        if vencedor == "computador":
            placar_computador = placar_computador + 1
        else:
            placar_usuario = placar_usuario + 1
        rodada += 1
    print("*** Final do campeonato! ***")
    print("Placar: Você",placar_usuario,"X",placar_computador,"Computador")

main()