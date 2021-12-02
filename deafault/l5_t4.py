import numpy 

a = int(input())
b = int(input())
N = int(input())
for t in numpy.linspace(a, b, N):
    x = abs(x0 + v0 * cos(a) * t)
    y = abs(y0 + v0 * sin(a) * t - ((g * t ** 2) / 2))
    answers[c, 0] = t
    answers[c, 1] = x
    answers[c, 2] = y
    c += 1
print(answers)