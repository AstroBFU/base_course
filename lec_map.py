def is_devide_by_three(a):
    return (a%3 == 0)

nums =[24, 65, 23, -32, 75]
result = list(map(is_devide_by_three, nums))

print(result)