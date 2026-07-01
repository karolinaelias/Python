agenda_telefonica = { }

while True:
    print("1 - Adicionar contato")
    print("2 - Consultar contato")
    print("3 - Exibir contatos cadastrados")
    print("4 - Encerrar o programa")

    opcao_escolhida = input("Digite a opção desejada:")

    if opcao_escolhida == "1":
        nome_contato = input("Digite o nome do contato:")
        if nome_contato in agenda_telefonica:
            print("Contato já cadastrado na agenda.")
        else:
            numero_contato = input("Digite o número de telefone:")
            agenda_telefonica[nome_contato] = numero_contato
            print("Contato cadastrado com sucesso!")
    elif opcao_escolhida == "2":
        contato = input("Digite o contato que deseja consultar:")
        if contato in agenda_telefonica:
            print(contato, "-", agenda_telefonica[contato])
        else:
            print("Contato não cadastrado na agenda")
    elif opcao_escolhida == "3":
        for contato, numero in agenda_telefonica.items():
            print(contato, "-", numero)
            print("-" * 30)
    elif opcao_escolhida == "4": 
        print("Encerrando programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")