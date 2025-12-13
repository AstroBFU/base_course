def s(a,b,n):
    y_m = []
    x_m = []
    for x in range(a,b,n):
        y=x**2
        y_m.append(y)
        x_m.append(x)
        #print(y)
    X = {'x':y_m}
    Y = {'y':x_m}
    return X, Y

print(s(2,8,1))
