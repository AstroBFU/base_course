counter = 0
def update(value):
    global counter
    result = counter + value
    print(f'{counter}+{value} = {result}')
update(1)
update(3)
update(5)