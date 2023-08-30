
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


sumaDiagonal = 0
for i in range(3):
    sumaDiagonal += matriz[i][i]


print("Matriz 3x3:")
for fila in matriz:
    print(fila)

print("La suma de los elementos en la diagonal es:", sumaDiagonal)
