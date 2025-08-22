#3. Crie uma função que verifique se um número é primo. 

def eh_primo(nm):
    if nm < 2:
        return False
    for i in range(2, int(nm ** 0.5) + 1):
        if nm % i == 0:
            return False
    return True

def continuar():
    resposta = input("Deseja verificar outro número? (s/n): ")
    if resposta == "s":
        saida()
    else:
        print("Até a próxima! ;)")
        exit()

def saida():
    n = int(input("Digite um numero: "))
    if eh_primo(n):
        print(f"{n} é primo")
        return continuar()
    else:
        print(f"{n} não é primo")
        return continuar()


saida()