len = [int(input()) for i in range(3)]
if (len[0] + len[1] > len[2]) and (len[1] + len[2] > len[0]) and (len[2] + len[0] > len[1]):
    print("Может существовать")
    if len[0] == len[1] == len[2]:
        print("Треугольник равносторонний")
    elif (len[0] == len[1]) or (len[1] == len[2]) or (len[2] == len[0]):
        print("Треугольник равнобедренный")
    else:
        print("Треугольник обычный")
else:
    print("Не может существовать")