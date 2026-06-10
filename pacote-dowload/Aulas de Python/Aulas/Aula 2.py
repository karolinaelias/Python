estoque = [
    {
        "nome": "Celular",
        "quantidade": 10, 
        "preco": 3000.00
    },
    {
        "nome": "Monitor",
        "quantidade": 5, 
        "preco": 799.99 
    },
    {
        "nome": "Tablet",
        "quantidade": 5, 
        "preco": 2000.00
    }
]

while True:

    # Exibição do menu principal
    print("\n==== SISTEMA DE CONTROLE DE ESTOQUE ====")
    print("1 - Visualizar Estoque Atual")
    print("2 - Registar Entrada de Produto")
    print("3 - Resgitrar Saída de Produto")
    print("4 - Sair do Sistema")
    
    opcao_ecolhida = input("Escolha uma opção:")
    
    # OPÇÃO 1 - VISUALIZAR ESTOQUE
    if opcao_ecolhida == "1":
        print("\n==== ESTOQUE ATUAL ====" )

        # Percorre todos os produtos cadastrados
        for produto in estoque: 
            print(f"Produto: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("------------------------------")

    # OPÇÃO 2 - REGISTRAR ENTRADA DE PRODUTO
    elif opcao_ecolhida == "2":
        nome_produto = input("Digite o nome do produto?: ")
        quantidade_entrada = int(input("Digite a quantidade de entrada: "))

        produto_encontrado = False

        for produto in estoque:

            # lower() evita diferenças entre maiúsculas e minúsculas
            if produto["nome"].lower() == nome_produto.lower():
                # Atualiza a quantidade do produto
                produto["quantidade"] += quantidade_entrada
                print("Quantidade atualizada com sucesso!")
                produto_encontrado = True
                # Interrompe o laço após encontrar o produto
                break

        # Caso o produto não exista no estoque
        if not produto_encontrado:
            print("Produto não encontrado.")

    # OPÇÃO 3 - REGISTRAR SAÍDA DE PRODUTO
    elif opcao_ecolhida == "3":
        nome_produto = input("Digite o nome do produto: ")
        quantidade_saida = int(input("Digite a quantidade de saída: "))

        produto_encontrado = False

        for produto in estoque:

            # Verifica se o nome digitado corresponde a um produto cadastrado
            if produto["nome"].lower() == nome_produto.lower():

                produto_encontrado = True

                # Verifica se existe quantidade suficiente para realizar a saída
                if produto["quantidade"] >= quantidade_saida:
                    # Realiza a subtração da quantidade
                    produto["quantidade"] -= quantidade_saida
                    print("Saída registrada com sucesso!")
                else:
                    print("Estoque insuficiente")
                break

        if not produto_encontrado:
            print("Produto não encontrado.")

    # OPÇÃO 4 - ENCERRAR SISTEMA
    elif opcao_ecolhida == "4":
        print("Encerrando o sistema...")
        # Interrompe o while True
        break

    # TRATAMENTO DE OPÇÃO INVÁLIDA
    else:
        print("Opção inválida. Tente novamente.")