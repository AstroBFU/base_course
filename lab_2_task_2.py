
b0 = int(input())
n = int(input())
q = int(input())

for iter in range(0, n, 1):
  print(f'iteration: {iter}')
  b1 = b0 * q
  print(b1)
  b0 = b1

