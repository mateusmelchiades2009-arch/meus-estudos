número = int(input("Digite um número inteiro: "))
if número <= 1:
    print("não primo")
else:
    divisor = 2
    eh_primo = True
    
    while divisor < número:
        if número % divisor == 0:
            eh_primo = False
        divisor = divisor + 1
    if eh_primo == True:
        print("primo")
    else:
        print("não primo")