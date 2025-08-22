#2. Validação de Login


senha_correta = "senha123"
tentativas = 3

while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Bem-vindo!")
        break
    else:
        tentativas -= 1
        print(f"Senha incorreta. Você ainda tem {tentativas} tentativas.")

if tentativas == 0:
    print("Acesso bloqueado.")
