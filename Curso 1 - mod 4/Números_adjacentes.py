numero = int(input("Digite um valor com varios digitos: ")) 

adjacentes = False
 
while numero > 0 and not adjacentes:
    ultimo = numero % 10
    penultimo = (numero // 10)%10
    if ultimo == penultimo:
        adjacentes = True
        
    numero = numero // 10

if adjacentes:
    print("sim")
else:
    print("não")