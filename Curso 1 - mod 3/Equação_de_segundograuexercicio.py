import math

a = float(input("Qual o valor de A?: "))
b = float(input("Qual o valor de B?: "))
c = float(input("Qual o valor de C?: "))
delta = (b**2) - 4 * a * c

if delta <0:
    print("esta equação não possui raízes reais")    
else:
   if delta == 0:
     raizum = (-b / (2 * a))
     print("a raiz desta equação é",raizum)
   else:
       raiz_1 = (-b + math.sqrt(delta))/(2*a)
       raiz_2 = (-b - math.sqrt(delta))/(2*a)
       if raiz_2 < raiz_1:
           print("as raízes da equação são",raiz_2,"e",raiz_1)
       else:
               print("as raízes da equação são",raiz_1,"e",raiz_2)