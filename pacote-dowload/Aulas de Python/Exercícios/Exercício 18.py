alunos = [
    {"nome": "Gustavo", "notas": [7.5, 10.0, 5.0, 6.5]},
    {"nome": "Isabela", "notas": [6.5, 5.0, 3.0, 7.5]},
    {"nome": "Karolina", "notas": [8.5, 9.0, 10.0, 8.0]}
]

for aluno in alunos:
    media = sum(aluno['notas']) / len(aluno['notas'])
    if media >= 7:
        situacao = "Aprovado"
        print(f"Nome: {aluno['nome']}")
        print(f"Média {media:.2f}")
        print(situacao)
        print("-" * 30)
