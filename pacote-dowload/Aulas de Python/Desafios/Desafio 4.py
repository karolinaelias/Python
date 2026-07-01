estoque = {
    "Notebook": 8,
    "Mouse": 45,
    "Teclado": 30,
    "Monitor": 5,
    "Fone": 60
}

maior_quantidade = 0
menor_quantidade = None

nome_maior = " "
nome_menor = " "
soma = 0
media = sum(estoque.values()) / len(estoque)

for produto, quantidade in estoque.items():
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        nome_maior = produto
    
    if menor_quantidade is None or quantidade < menor_quantidade:
        menor_quantidade = quantidade
        nome_menor = produto

for produto, quantidade in estoque.items():
    soma += quantidade

print(f"Produto com maior estoque: {nome_maior} ({maior_quantidade} unidades)")
print (f"Produto com menor estoque: {nome_menor} ({menor_quantidade} unidades)")
print (f"Total de itens em estoque: {soma}")
print(f"Média de itens por produto: {media}")