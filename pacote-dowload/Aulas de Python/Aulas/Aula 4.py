alunos = [
    {
        "nome": "João",
        "notas": [8.5, 7.0, 9.0]
    },
    {
        "nome": "Maria",
        "notas": [10.0, 6.0, 9.5]
    },
    {
        "nome": "Pedro",
        "notas": [7.5, 6.0, 6.5]
    }
]

def calcular_media(notas):

    media = sum(notas) / len(notas)

    return media

def verificar_aprovacao(media, media_minima=7.0):

    if media >= media_minima:
        return "Aprovado"

    return "Reprovado"

def gerar_relatorio(alunos):

    print("==== RELATÓRIO DOS ALUNOS ====")

    for aluno in alunos:
        media = calcular_media(aluno["notas"])

        situacao = verificar_aprovacao(media)

        print(f"Nome: {aluno['nome']}")
        print(f"Média: {media:.2f}")
        print(f"Situação: {situacao}")
        print("-" * 30)

gerar_relatorio(alunos)    