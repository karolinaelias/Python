nota_aluno = float(input("Digite a sua nota: "))

if nota_aluno >= 7:
    print("Aprovado!")
elif nota_aluno >= 5:
    print("Em recuperação")
else:
    print("Reprovado")