#4. Desenvolva um programa que leia uma lista de números e mostre a média deles.

def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def main():
    
    lista_numeros = []
    while True:
        entrada = int(input("Digite um número: "))
        lista_numeros.append(entrada)

        media = calcular_media(lista_numeros)
        print(f"A média é: {media}")

        continuar = input("Deseja adicionar outro número? (s/n): ").strip().lower()
        if continuar != 's':
            break
        elif continuar == 'n':
            exit()
            return
main()