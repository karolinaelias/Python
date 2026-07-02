senha_correta = "4321"
tentativas = 0
tentativa_total = 4

senha_digitada = input("Digite a senha: ")

while tentativas < 4:
    tentativas += 1 
    tentativa_total -= 1

    if senha_digitada == senha_correta:
        print("Cofre aberto com sucesso!")
        break
    elif tentativas == 4:
        print("Cofre bloqueado.")
    else:
        print (f"Senha incorreta. Restam {tentativa_total} tentativa(s).")
        senha_digitada = input("Digite a senha: ")