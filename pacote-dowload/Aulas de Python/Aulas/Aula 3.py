import random

def iniciar_jogo():
    """
    Escolhe uma palavra aleatória e cria
    as estruturas iniciais do jogo.
    """

    lista_palavras = [
        "CAVALO",
        "GATO",
        "CACHORRO",
        "VACA",
        "FORMIGA"
    ]

    palavra_secreta = random.choice(lista_palavras)

    palavra_oculta = ["_"] * len(palavra_secreta)

    # Set utilizado para evitar letras repetidas
    letras_tentadas = set()

    return palavra_secreta, palavra_oculta, letras_tentadas


def verificar_letra(
    letra_digitada,
    palavra_secreta,
    palavra_oculta
):
    """
    Verifica se a letra existe na palavra
    e atualiza a palavra oculta.
    """

    letra_encontrada = False

    for indice in range(len(palavra_secreta)):

        if palavra_secreta[indice] == letra_digitada:

            palavra_oculta[indice] = letra_digitada

            letra_encontrada = True

    return letra_encontrada


# Inicialização do jogo
palavra_secreta, palavra_oculta, letras_tentadas = iniciar_jogo()

maximo_tentativas = 6
tentativas_erradas = 0

print("===== JOGO DA FORCA =====")

while (
    tentativas_erradas < maximo_tentativas
    and "_" in palavra_oculta
):

    print("\nPalavra:", " ".join(palavra_oculta))

    print("Letras tentadas:", letras_tentadas)

    print(
        "Tentativas restantes:",
        maximo_tentativas - tentativas_erradas
    )

    letra_digitada = input(
        "Digite uma letra: "
    ).upper()

    # Verifica se a letra já foi utilizada
    if letra_digitada in letras_tentadas:

        print("Você já tentou essa letra.")

        continue

    # Adiciona a letra no conjunto
    letras_tentadas.add(letra_digitada)

    acertou = verificar_letra(
        letra_digitada,
        palavra_secreta,
        palavra_oculta
    )

    # Caso a letra exista na palavra
    if acertou:

        print("Letra correta!")

    # Caso a letra não exista
    else:

        print("Letra incorreta!")

        tentativas_erradas += 1


# Verifica resultado final
if "_" not in palavra_oculta:

    print("\nParabéns! Você venceu!")

else:

    print("\nVocê perdeu!")

    print(
        "A palavra secreta era:",
        palavra_secreta
    )

print("Fim de jogo.")