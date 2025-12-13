x0 = 10 # Переменная в глобальной области видимости


def move(t):
    x = x0 * t # Переменная в локальной области видимости
    return x

  
print(move(3))
# print(x)

a = 'Good'

def test_local_data():
    a = 'Bad'
    print(a,id(a))

test_local_data()
print(a,id(a))
 
