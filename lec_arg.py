def my_func(a, b):
    x = 3 * a - b
    return x


#tmp = my_func()

def my_func(a=1, b=0):
    x = 3 * a - b
    return x


print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b=3))
print(my_func(b=3, a=9))


def my_func(a, b=0):
    x = 3 * a - b
    return x

# ТАК НЕЛЬЗЯ!!!
# def my_func(a=0, b):
#     x = 3 * a - b
#     return x

def my_func(*args):
    x = (args[0] + args[1]) / len(args)
    return x


print(my_func(3, 4))
print(my_func(3, 4, 8))


def my_func(**kwrgs):
    x = len(kwrgs) * (kwrgs['obj_1'] - kwrgs['obj_2'])
    return x


print(my_func(obj_1=3, obj_2=4))
print(my_func(obj_1=3, obj_2=4, obj_3=8))