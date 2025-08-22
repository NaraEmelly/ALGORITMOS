#1. Faça um programa que leia dois números e mostre qual é o maior. 


print("Escreva um numero abaixo")

def num_maior():

    x =  int(input("\nPrimeiro número: "))
            
    y =  int(input("Segundo número: "))



    if x > y :
        print(f"Esse é seu numero maior: {x}")

    elif y > x :
        print(f"Esse é seu numero maior: {y}")

    elif x >= y:
        print(f"Eles possuem o mesmo valor")
    else:
        print("Erro, tente novamente")
        return num_maior()

num_maior()





    
    