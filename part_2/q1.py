#1. Cálculo de Complexidade Simples


def calcular_soma(n):
    soma = 0
    operacoes = 0
    for i in range(1, n + 1):
        soma += i
        operacoes += 1
    return soma, operacoes

n = int(input("Digite um número: "))
soma, operacoes = calcular_soma(n)
print(f"Soma: {soma}")
print(f"Operações básicas (somas) realizadas: {operacoes}")
print(f"Fórmula matemática: {n * (n + 1) // 2}")

calcular_soma(n)