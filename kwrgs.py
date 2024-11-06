def fun(**kwrgs):
    return 3 * kwrgs['a'] - kwrgs['b']
print(fun(a=3, b=4))