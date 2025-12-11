import random as rand
import numpy
N = int(input())
mass1, mass2, mass3 = [rand.randint(0,100) for i in range(N)], [rand.randint(0,100) for i in range(N)],[rand.randint(0,100) for i in range(N)]
print(max(mass1 + mass2 + mass3))
print(sum(mass1 + mass2 + mass3))