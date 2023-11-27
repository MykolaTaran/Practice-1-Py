def calculate_series(n):
    total_sum = 0
    count_elements = 0

    for x in range(1, n + 1):
        element = 1
        for i in range(1, 2 * x):
            element *= (2 * x - 1)

        total_sum += element
        count_elements += 1

    return total_sum, count_elements

# Задана величина n
n_value = 20

# Обчислення суми та кількості елементів ряду
result_sum, result_count = calculate_series(n_value)

# Виведення результатів
print(f"Сума елементів ряду: {result_sum}")
print(f"Кількість елементів ряду: {result_count}")