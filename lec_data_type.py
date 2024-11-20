def changer(a , b):
    a = 2
    b[0] = 'Good'

x = 10
L = [1, 2]

changer(x, L)
print(x)
print(L)

L = [1, 2]
changer(x, L[:])
# complex
x = 3
y = 4

z = complex(x,y)
print(z)

w = complex(y, x)
print(z + w)
# str
s = 'hello'
print(s[0])

#s[0] = 'p'
#print(s)
#tuple
t = (1,4,9)
print(t)
print(t[0])
#t[0] = 3
#list
l = [1,4,9]
print(l)
print(l[0])
l[0] = 3
print(l)
# dict
d = {'a1':4, 4:'a1', 'str':'Hello'}
print(d['a1'])
print(d['str'])
d['str'] = 'Good'