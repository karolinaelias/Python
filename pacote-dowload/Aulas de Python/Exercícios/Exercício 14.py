palavra = input("Digite uma palavra: ")
vogais = "aeiouáàãéêíõóú"
contador = 0

for letra in palavra.lower():
    if letra in vogais:
        contador += 1

print(contador)