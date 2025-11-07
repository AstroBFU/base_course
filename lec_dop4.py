n = int(input("Vvedite chislo: "))
c2 = 0
c3 = 0
c5=0
c7 = 0
while n % 2 == 0:
    c2 +=1
    n = n/2
while n % 3 == 0:
    c3+=1
    n = n/3
while n % 5 == 0:
    c5+=1
    n = n/5
while n % 7 == 0:
    c7+=1
    n = n/7
    
print(f"2: {c2}; 3: {c3}; 5: {c5}; 7: {c7}")