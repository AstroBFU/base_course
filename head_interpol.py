import matplotlib.pyplot as plt 
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

t1=np.linspace(np.pi/2, np.pi/4.8 ,200)
x1=0 + 380*np.cos(t1)
y1=800-430*np.sin(t1)

t2=np.linspace(np.pi, np.pi/2.6 ,200)
x2=450+150*np.cos(t2)
y2=530 -40*np.sin(t2)

x = np.append(x1, x2)
y = np.append(y1, y2)

x3 = [510,570.1]
y3 = [490.1,360]

x = np.append(x, x3)
y = np.append(y, y3)

t4=np.linspace(np.pi+np.pi/6, np.pi+np.pi/2.3 ,200)
x4=420-175*np.cos(t4)
y4=320-90*np.sin(t4)


x = np.append(x, x4)
y = np.append(y, y4)

t5=np.linspace(np.pi+np.pi/2,np.pi/2  ,200)
x5=480+70*np.cos(t5)
y5=380 -30*np.sin(t5)


x = np.append(x, x5)
y = np.append(y, y5)

x7 = [550,700]
y7 = [270.1,330]


x = np.append(x, x7)
y = np.append(y, y7)

x8 = [700.1,730]
y8 = [330.1,410]


x = np.append(x, x8)
y = np.append(y, y8)

x9 = [730.1,650]
y9 = [410.1,680]


x = np.append(x, x9)
y = np.append(y, y9)

x10 = [650.1,730]
y10 = [680.1,690]


x = np.append(x, x10)
y = np.append(y, y10)

x11 = [730.2,750]
y11 = [690.1,850]


x = np.append(x, x11)
y = np.append(y, y11)

t12=np.linspace(np.pi, np.pi/4.8 ,200)
x12=1000.1 +250*np.cos(t12)
y12=850.1-90*np.sin(t12)


x = np.append(x, x12)
y = np.append(y, y12)

x13 = [1199.1,1199.02]
y13 = [800.01,899.03]

x = np.append(x, x13)
y = np.append(y, y13)


x14 = [0,1199]
y14= [899.1,899.2]

x = np.append(x, x14)
y = np.append(y, y14)

x15 = [0,0]
y15= [900,370]

x = np.append(x, x15)
y = np.append(y, y15)

# x = [0, 300,530,580,440,440,540,720,780,680,790,800,1200,1200,0,0]
# y = [370,520,450,380,390,330,280,370,390,630,640,840,790,900,900,370]


spline_coords, figure_spline_part = interpolate.splprep([x,y], s = 0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)
# plt.plot(spline_curve[0], spline_curve[1], color  = 'g', lw = 4)

curve_coords = []
for i in range (len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i],spline_curve[1][i] ])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 500

x_pictures_limits=[0, 1200]
y_pictures_limits=[0, 1000]

points_coords = []

for x_point_coord in np.linspace (*x_pictures_limits,points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point (x_point_coord, y_point_coord)
        if p.within(polygon):
            plt.plot (x_point_coord, y_point_coord, 'ro', ms = 0.5)
        
    


plt.plot(x, y, 'bo')
plt.plot(spline_curve[0], spline_curve[1],'g')
plt.axis('equal')
plt.savefig('INTERPOL.png')

