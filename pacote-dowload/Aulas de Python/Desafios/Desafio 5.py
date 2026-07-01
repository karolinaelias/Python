lista = [ ]

while True:
    print("1 - Adicionar nome na lista")
    print("2 - Exibir nomes cadastrados")
    print("3 - Buscar nome cadastrado")
    print("4 - Editar nome cadastrado")
    print("5 - Remover nome da lista")
    print("6 - Encerrar programa")
    
    opcao_escolhida = input("Escolha uma opção:")

    if opcao_escolhida == "1":
        novo_nome = input("Digite o nome a ser cadastrado:")
        if novo_nome == "":
            print("Nome inválido.")
        else:
            lista.append(novo_nome)
            print("Nome cadastrado com sucesso!")
    elif opcao_escolhida == "2":
        if len(lista) == 0:
            print("Nenhum nome cadastrado ainda.")
        else:
            print("==== Nomes Cadastrados ====")
            for nome in lista:
                print(nome)
                print("-" * 10)
    elif opcao_escolhida == "3":
        busca_nome = input("Digite o nome a ser procurado:")
        if busca_nome in lista:
            print("O nome está cadastrado na lista.")
        else:
            print("O nome não está cadastrado na lista.")
    elif opcao_escolhida == "4":
        nome_atual = input("Digite o nome a ser editado:")
        if nome_atual in lista:
            posicao = lista.index(nome_atual)
            novo_nome = input("Digite o novo nome:")
            lista[posicao] = novo_nome
            print("Nome alterado com sucesso!")
        else:
            print("Nome não encontrado.")
    elif opcao_escolhida == "5":    
        nome = input("Digite o nome a ser removido:")
        if nome in lista:
            lista.remove(nome)
            print("Nome removido com sucesso!")
        else:
            print("O nome não está cadastrado na lista")
    elif opcao_escolhida == "6": 
        print("Encerrando programa...")
        break
    else: 
        print("Opção inválida. Tente novamente.")