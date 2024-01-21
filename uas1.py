def knapsack_backtracking(weights, values, capacity):
    n = len(weights)
    best_value = [0]
    best_combination = [0] * n
    current_value = 0
    current_weight = 0
    current_combination = [0] * n

    def explore(k):
        nonlocal current_value, current_weight

        if k == n:
            if current_value > best_value[0] and current_weight <= capacity:
                best_value[0] = current_value
                best_combination[:] = current_combination[:]
            return

        # Include the item
        current_combination[k] = 1
        current_weight += weights[k]
        current_value += values[k]
        explore(k + 1)

        # Exclude the item
        current_combination[k] = 0
        current_weight -= weights[k]
        current_value -= values[k]
        explore(k + 1)

    explore(0)
    return best_combination

# Barang yang tersedia
weights = [4, 3, 2, 1, 1]
values = [8, 5, 6, 3, 4]

# Batasan berat tas
capacity = 8

# Mendapatkan kombinasi barang dengan nilai maksimum
result = knapsack_backtracking(weights, values, capacity)

# Menampilkan hasil
print("Barang yang harus dibawa oleh Ucup:")
for i in range(len(result)):
    if result[i] == 1:
        print(f"Barang {i+1} (Bobot: {weights[i]} kg, Nilai: {values[i]})")