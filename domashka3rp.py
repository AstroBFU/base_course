import time
start = time.time()
N = int(input())
M = int(input())
for i in range(M):
    print(i)
    time.sleep(1)
    for el in range(N):
        print(el)
        time.sleep(1)
finish = time.time()
print(f'Время выполнения {finish-start}')