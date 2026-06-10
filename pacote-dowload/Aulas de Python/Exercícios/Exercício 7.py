alunos = [
    {
        "nome": "Gustavo",
        "notas": [7.5, 10.0, 5.0, 6.5] 
    },
    {
        "nome": "Isabela",
        "notas": [6.5, 5.0 ,3.0 ,7.5]
    },
    {
        "nome": "Karolina",
        "notas": [8.5, 9.0, 10,0, 8,0]
    }
]

print("==== Informações Alunos ====")

for aluno in alunos:
    print(f"Nome: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print("-" * 30)