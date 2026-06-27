
def dimensoes(matriz):
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    print(f"{num_linhas}X{num_colunas} ")
minha_matriz = [[1, 2,], [4, 5], [7, 8]]
dimensoes(minha_matriz)