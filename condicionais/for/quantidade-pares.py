quantidades_pares= 0
for numero in range(2, 51 , 2):
    quantidades_pares += 1 

print(quantidades_pares)

for indice, numero in enumerate(range(2, 51, 2)):
    print(indice + 1, numero )
