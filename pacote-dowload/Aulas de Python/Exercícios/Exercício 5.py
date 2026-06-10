numeros = [2,20,2,55,3,2,0,5,2,2,]
valor_procurado = 2

contador = 0

for numero in numeros:
    if numero == valor_procurado:
        contador += 1

print(f"O número aparece {contador} vezes na lista.")