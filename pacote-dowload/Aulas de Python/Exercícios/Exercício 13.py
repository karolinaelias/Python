senha = "senha123"
senha_diigtada = input("Digite a senha: ")


while senha_usuario != senha:
    print("Senha incorreta tente novamente.")
    senha_usuario = input("Digite a senha: ")

print("Acesso liberado.")