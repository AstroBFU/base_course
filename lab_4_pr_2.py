def mult(a):
    c=1
    for x in a:
        c = c + x
    z = c * len(a)
    print(z)
    

mult([3,4,7,8])