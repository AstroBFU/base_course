def final_func(a: float, b: int=0, c=1, *args, **kwargs):
    print(f'a: {a}, b: {b}, c: {c}')
    print(f'args: {args}, kwargs: {kwargs} \n')
    return 'done'


final_func(1)
final_func(1, 'Good', 4)
final_func(1, 2, 4, 5)
final_func(1, 2, 4, 5, 1, 2, 4, 5)
final_func(1, red=0, green=1, blue=0)
final_func(1, 2, 4, 5, 1, red=0, green=1, blue=0)