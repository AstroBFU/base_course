def changer(a,b):
  a=2  
  b[0]='Good'
x=10
l=[1,2]

changer(x,l)
print(x)
print(l)

l=[1,2]
changer(x,l[:])
print(l)

def my_func(a,b):
  x=3*a-b
  return x
#print(my_func())

def my_func(a=1,b=0):
  x=3*a-b
  return x
print(my_func())

print(my_func(1,4))

print(my_func(6))

print(my_func(b=7))

print(my_func(b=3,a=0))


