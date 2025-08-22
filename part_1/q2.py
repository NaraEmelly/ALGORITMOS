#2. Escreva um algoritmo que calcule a tabuada de um número digitado pelo usuário.


def tabuada():
    
    num = int(input("Escreva o numero: "))
    
    for i in range(1, 11):
     resultado = num * i
     print(f"{num} x {i} = {resultado}" )
        
    
tabuada()
    


