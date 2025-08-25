#5. Verificação de CPF (simplificada)

cpf = input("Digite seu Cpf aqui: ")

if cpf.isdigit()and len(cpf) == 11:
    print("Cpf Válido")
else:

    print("Cpf Inválido")
