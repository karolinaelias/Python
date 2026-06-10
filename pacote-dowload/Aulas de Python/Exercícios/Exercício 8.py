alunos = {
    "Ana": 8.5,
    "Pedro": 6.0,
    "Maria": 9.0,
    "João": 7.5
}

nome = input("Digite o nome do aluno: ")

if nome in alunos:
    print("Nota:", alunos[nome])
else:
    print("Aluno não encontrado.")
