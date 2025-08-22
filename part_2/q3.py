#3. Estatísticas de Notas


def estatisticas_notas(notas):

    soma = sum(notas)
    media = soma / len(notas)
    maior = max(notas)
    menor = min(notas)
    acima_media = [n for n in notas if n > media]
    percentual_acima = (len(acima_media) / len(notas)) * 100

    print(f"Média: {media:.2f}")
    print(f"Maior nota: {maior:.2f}")
    print(f"Menor nota: {menor:.2f}")
    print(f"Percentual de alunos acima da média: {percentual_acima:.2f}%")

    for i in range(len(notas)):
        print(f"Aluno: {alunos_nome[i]}, Nota: {notas[i]:.2f}")

alunos_nome = ["Ana", "Beatriz", "Silva", "Chris", "Emelly"]

notas = [10.0 , 8.0 , 3.0 , 9.5, 7.8]

estatisticas_notas(notas)