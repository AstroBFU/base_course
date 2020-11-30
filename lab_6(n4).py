  
import matplotlib.pyplot as plt

def stairs(N = 0, title="stairs"):
    x = [0]
    y = [0]
    
    for i in range(N):
        x += [i, i + 1]
        y += [i + 1]*2
    
    plt.plot(x, y, color='k', label="stairs")
    
    plt.legend()
    plt.title(title)
    
    plt.show()

num = int(input("num = "))
stairs(num)