import matplotlib.pyplot as plt 
import numpy as np
plt.arrow(0,0,4,4,width=0.02)
plt.savefig('vector.png')
plt.close()
x,y=np.meshgrid(np.linspace(-5,5,10) ,np.linspace(-5,5,10) )
u = 1
v = -1
plt.quiver(x,y,u,v)
plt.title('векторное поле скоростей, v={1:-1},м/с')
plt.xlabel('координата x,м')
plt.ylabel('координата y,м')
plt.savefig('vector_field_1.png')
plt.close()



u = x / np.sqrt(x**2+ y**2)
v = y / np.sqrt(x**2+ y**2)
plt.quiver(x,y,u,v)
plt.title('векторное поле скоростей, v={1:-1},м/с')
plt.xlabel('координата x,м')
plt.ylabel('координата y,м')
plt.savefig('vector_field_2.png')
plt.close()

u = - y / np.sqrt(x**2+ y**2)
v =  x / np.sqrt(x**2+ y**2)
plt.quiver(x,y,u,v)
plt.title('векторное поле скоростей, v={1:-1},м/с')
plt.xlabel('координата x,м')
plt.ylabel('координата y,м')
plt.savefig('vector_field_3.png')
plt.close()

u = - y / np.sqrt(x**2+ y**2)+y
v =  x / np.sqrt(x**2+ y**2)+x
plt.quiver(x,y,u,v)
plt.title('векторное поле скоростей, v={1:-1},м/с')
plt.xlabel('координата x,м')
plt.ylabel('координата y,м')
plt.savefig('vector_field_4.png')
plt.close()