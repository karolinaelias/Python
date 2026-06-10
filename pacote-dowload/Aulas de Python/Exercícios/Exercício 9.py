alunos = {
    "Ana": 8.5,
    "Pedro": 6.0,
    "Maria": 9.0,
    "João": 7.5
}

soma = 0

for nota in alunos.values():
    soma += nota

    media = soma / len(alunos)

    print("Média da turma:", media )