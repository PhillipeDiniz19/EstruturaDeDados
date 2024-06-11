from collections import Counter


fila1 = [1, 2, 3, 4, 5, 5, 6]
fila2 = [3, 4, 5, 6, 7, 8, 8]


numeros_totais = fila1 + fila2

contador = Counter(numeros_totais)

numeros_duplicados = [numero for numero, quantidade in contador.items() if quantidade > 1]

print("Números duplicados nas filas:", numeros_duplicados)
