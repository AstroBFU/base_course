def print_table(n, m):
    add_symbols_to = "{:<" + str(len(str(m * n))) + "}"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(add_symbols_to.format(i * j), end=" ")
        print()

for i in range(3, 20):
    print(f"\nТаблица умножения {i} X {i}:")
    print_table(i, i)

print(f"\n\nТаблица умножения 9 X 9:")
print_table(9, 9)