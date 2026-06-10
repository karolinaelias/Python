estoque = [
    {
        "nome": "Sabonete",
        "quantidade": 10
    },
    {
        "nome": "Pasta de dente",
        "quantidade": 0
    },
    {
        "nome": "Escova de dente",
        "quantidade": 0
    },
    {
        "nome": "Gilete",
        "quantidade": 5
    }
]

for produto in estoque:
    if produto["quantidade"] > 0:
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")