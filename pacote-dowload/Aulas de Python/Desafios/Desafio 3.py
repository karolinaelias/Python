alunos = {
    "Ana": 8.5,
    "Pedro": 6.0,
    "Maria": 9.0,
    "João": 7.5
}

menor_nota = min(alunos.values())
maior_nota = max(alunos.values())
media = sum(alunos.values()) / len(alunos) 

print(f"A maior nota da turma é: {maior_nota}")
print(f"A menor nota da turma é: {menor_nota}")    
print(f"A média da turma é: {media}")