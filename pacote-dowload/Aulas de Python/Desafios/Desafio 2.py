livros = [
    {"nome": "As Crônicas de Nárnia", "autor": "C. S. Lewis", "disponibilidade": "Disponível"},
    {"nome": "A menina que não saba ler", "autor": "John Harding", "disponibilidade": "Indisponível"},
    {"nome": "Garota Exemplar", "autor": "Gillian Flynn", "disponibilidade": "Disponível"},
    {"nome": "O Deus que destrói sonhos", "autor": "Rodrigo Bibo", "disponibilidade": "Disponível"},
    {"nome": "Como ser um cristão inútil", "autor": "Rodrigo Bibo", "disponibilidade": "Disponível"},
    {"nome": "A cidade e as serras", "autor": "Eça de Queirós", "disponibilidade": "Indisponível"}
]

print("==== LIVROS DISPONÍVEIS PARA EMPRÉSTIMO ====")

for livro in livros:
    if livro['disponibilidade'] == 'Disponível':
        print(f"Nome: {livro['nome']}")
        print(f"Autor: {livro['autor']}")
        print("-" * 30)
