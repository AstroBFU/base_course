def s(*i):
    return sum(i)/len(i)
print(s(1, 2, 3, 4, 5))

def mean_p(*i):
    s = 0
    for arg in args:
        s+=arg
    return s/len(args)
args = (1, 2, 3, 4, 5)
mean = mean_p(1, 2, 3, 4, 5)
print(mean)
  