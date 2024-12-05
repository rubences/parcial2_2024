def knapsack(max_weight, weights, values, n):
    # Crear una tabla para almacenar los valores máximos
    K = [[0 for x in range(max_weight + 1)] for x in range(n + 1)]

    # Construir la tabla K[][] de abajo hacia arriba
    for i in range(n + 1):
        for w in range(max_weight + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Almacenar el resultado del valor máximo
    res = K[n][max_weight]
    print(f"Valor máximo que puede llevar Luke: {res}")

    # Encontrar los elementos que se incluyen en la mochila
    w = max_weight
    items_selected = []
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            items_selected.append(i - 1)
            res = res - values[i - 1]
            w = w - weights[i - 1]

    return items_selected

# Datos del problema
values = [500, 200, 400, 300, 350, 1000]
weights = [15, 5, 8, 4, 3, 10]
max_weight = 50
n = len(values)

# Resolver el problema de la mochila
items_selected = knapsack(max_weight, weights, values, n)

# Mostrar los objetos seleccionados
items = ["Blaster", "Raciones de comida", "Cloak Jedi", "Mapa Estelar", "Comunicador Galactic", "Sable de luz de Luke"]
print("Objetos seleccionados para llevar en la mochila:")
for i in items_selected:
    print(f"{items[i]}: valor = {values[i]}, peso = {weights[i]}")