n = int(input())
list = [1, 1]

for i in range(n-1):
    list.append(list[i] + list[i+1])
for i in range(len(list)):
    print(int(list[i]))