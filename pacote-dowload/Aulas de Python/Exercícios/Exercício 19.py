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

for produto in estoque:
    maior_preco = max({produto['preco']})
    break

print(f"Produto mais caro: {produto['nome']}")
print(f"Preço: {maior_preco: .2f}")