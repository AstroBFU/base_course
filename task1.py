def arithmetic_mean(arr):
    x = 0
    for i in range(len(arr)):
        x += arr[i]
    return x / len(arr)

array = [1, 2, 3, 4, 5]

print(arithmetic_mean(array))