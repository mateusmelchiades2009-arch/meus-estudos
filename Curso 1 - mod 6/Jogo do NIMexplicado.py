def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")  # Exibe a mensagem de boas-vindas
    escolha = 0  # Cria a variável escolha valendo 0 para iniciar o loop
    while escolha != 1 and escolha != 2:  # Mantém o menu rodando enquanto o usuário não digitar 1 ou 2
        print("1 - para jogar uma partida isolada")  # Mostra a opção 1 no menu
        print("2 - para jogar um campeonato")  # Mostra a opção 2 no menu
        escolha = int(input(""))  # Lê a opção do usuário e converte para número inteiro
        if escolha == 1:  # Se a escolha for igual a 1
            print("Voce escolheu uma partida isolada!")  # Avisa que a partida isolada foi escolhida
            partida()  # Chama a função partida para iniciar o jogo de verdade
        elif escolha == 2:  # Se a escolha for igual a 2
            print("Voce escolheu um campeonato!")  # Avisa que o campeonato foi escolhido
            campeonato()  # Chama a função campeonato para iniciar o torneio
        else:  # Se digitar qualquer outra coisa
            print("Opção inválida! Tente novamente.")  # Avisa que a opção não existe
    return escolha  # Devolve o valor final da escolha (1 ou 2)

def computador_escolhe_jogada(n, m):
    pecas_retiradas = 1  # Começa testando a menor jogada possível, tirar 1 peça
    while pecas_retiradas <= m:  # Cria um loop que testa valores de jogada até o limite m
        if (n - pecas_retiradas) % (m + 1) == 0:  # Testa se a jogada deixa um número de peças múltiplo de m+1
            return pecas_retiradas  # Se deixar o número ideal, o computador faz essa jogada e sai da função
        else:  # Se essa quantidade não for a ideal
            pecas_retiradas = pecas_retiradas + 1  # Aumenta o teste para tentar tirar mais uma peça
    return m  # Se nenhuma jogada foi perfeita, o computador tira o máximo permitido (m)

def usuario_escolhe_jogada(n, m):
    jogada_valida = False  # Cria uma variável de controle dizendo que a jogada ainda não é válida
    while not jogada_valida:  # Repete o loop enquanto a jogada não for válida
        jogada = int(input("Quantas peças você vai tirar? "))  # Pede a jogada do usuário e converte em inteiro
        if jogada <= m and jogada > 0 and jogada <= n:  # Checa se a jogada obedece o limite m, é maior que zero e não tira mais do que há no tabuleiro
            jogada_valida = True  # Se passar em todas as regras, marca a jogada como válida para encerrar o loop
        else:  # Se quebrar alguma regra
            print("Oops! Jogada inválida! Tente de novo.")  # Mostra a mensagem de erro na tela
            jogada_valida = False  # Mantém a jogada como inválida para o loop continuar rodando
    return jogada  # Devolve a quantidade de peças que o usuário escolheu tirar

def partida():
    n = int(input("Quantas peças? "))  # Pede a quantidade total de peças inicial do jogo
    m = int(input("Limite de peças por jogada? "))  # Pede o limite máximo de peças por rodada
    vez_do_computador = False  # Cria a variável de turno começando como falsa por padrão
    if n % (m + 1) == 0:  # Aplica a regra matemática: se o total for múltiplo de m+1, o usuário começa
        print("Você começa!")  # Exibe a mensagem avisando o usuário
        vez_do_computador = False  # Define o turno explicitamente para o usuário (False)
    else:  # Caso contrário (se não for múltiplo)
        print("Computador começa!")  # Exibe a mensagem avisando que a máquina começa
        vez_do_computador = True  # Define o turno para o computador (True)
    while n > 0:  # Começa o loop do jogo, que continuará rodando enquanto houver peças no tabuleiro
        if vez_do_computador == True:  # Se for o turno do computador
            jogada = computador_escolhe_jogada(n, m)  # Chama a função inteligente do computador e armazena a jogada
            if jogada == 1:  # Se a máquina escolheu tirar apenas 1 peça
                print("O computador tirou uma peça")  # Mostra a frase no singular
            else:  # Se a máquina tirou 2 ou mais peças
                print("O computador tirou", jogada, "peças.")  # Mostra a frase no plural com a quantidade
            n = n - jogada  # Atualiza o tabuleiro subtraindo as peças que o computador retirou
            vez_do_computador = False  # Muda o turno para False para passar a vez para o usuário
        else:  # Se não for a vez do computador (ou seja, vez do usuário)
            jogada = usuario_escolhe_jogada(n, m)  # Chama a função de validação do usuário e armazena a jogada
            if jogada == 1:  # Se o usuário escolheu tirar apenas 1 peça
                print("Você tirou uma peça")  # Mostra a frase no singular
            else:  # Se o usuário tirou 2 ou mais peças
                print("Você tirou", jogada, "peças.")  # Mostra a frase no plural com a quantidade
            n = n - jogada  # Atualiza o tabuleiro subtraindo as peças que o usuário retirou
            vez_do_computador = True  # Muda o turno para True para passar a vez para o computador
        if n > 0:  # Após a jogada e a conta, se ainda sobrarem peças no tabuleiro
            if n == 1:  # Se sobrou exatamente 1 peça
                print("Agora resta apenas uma peça no tabuleiro.")  # Mostra o placar no singular
            else:  # Se sobraram 2 ou mais peças
                print("Agora restam", n, " peças no tabuleiro.")  # Mostra o placar no plural com o saldo restante
    print("Fim do jogo! O computador ganhou!")  # Fora do while: quando n chega a 0, exibe que a máquina venceu
    return "computador"  # Retorna o texto "computador" para indicar quem foi o vencedor da partida

def campeonato():
    placar_usuario = 0  # Inicia os pontos do usuário valendo zero
    placar_computador = 0  # Inicia os pontos do computador valendo zero
    rodada = 1  # Define que o campeonato começa na rodada número 1
    while rodada <= 3:  # Cria um loop para rodar o campeonato até completar 3 rodadas
        print("*** Rodada", rodada, "***")  # Exibe o título indicando o número da rodada atual
        vencedor = partida()  # Executa uma partida inteira e guarda quem venceu na variável vencedor
        if vencedor == "computador":  # Se o retorno da partida foi "computador"
            placar_computador = placar_computador + 1  # Adiciona 1 ponto ao placar da máquina
        else:  # Caso o vencedor seja o usuário (o que não acontece devido à estratégia perfeita)
            placar_usuario = placar_usuario + 1  # Adiciona 1 ponto ao placar do usuário
            rodada += 1  # Avança o número da rodada (soma 1 na variável rodada)
    print("*** Final do campeonato! ***")  # Fora do loop: avisa que as 3 rodadas terminaram
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")  # Exibe o placar final do campeonato

main()  # Chama a função inicial do topo para dar a largada e rodar todo o sistema do arquivo