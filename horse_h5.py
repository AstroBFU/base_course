import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom
import h5py

x15= [0.01,0.02]
y15 = [370.01,899]




t1=np.linspace(np.pi/2, np.pi/4.8 ,200)
x1=0 + 380*np.cos(t1)
y1=800-430*np.sin(t1)

x = np.append(x15, x1)
y = np.append(y15, y1)


 

t2=np.linspace(np.pi, np.pi/2.6 ,200)
x2=450+150*np.cos(t2)
y2=530 -40*np.sin(t2)


x = np.append(x, x2)
y = np.append(y, y2)

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

spline_coords, figure_spline_part = interpolate.splprep([x,y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_numper_per_side = 1000
x_pictures_limits = [0.0, 1200.0]
y_pictures_limits = [0.0, 900.0]

points_coords = []
for x_point_coord in np.linspace(*x_pictures_limits, points_numper_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_numper_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])


float_type=np.float64
int_type=np.int32

picture_size_x = max(x_pictures_limits)-min(x_pictures_limits)
picture_size_y= max(y_pictures_limits)-min(y_pictures_limits)
picture_size=max(picture_size_x,picture_size_y)

box_size=100*picture_size

gas_part_num=len(x_p)
gas_coords=np.zeros([gas_part_num,3], dtype=float_type)

gas_vel=np.zeros([gas_part_num,3], dtype=float_type)

gas_masses=np.ones(gas_part_num, dtype=float_type)

for i in range(len(x_p)):
     gas_coords[i,0]=x_p[i]/picture_size+box_size/2
     gas_coords[i][1]=y_p[i]/picture_size+box_size/2
     gas_vel[i][0]=float_type(0.001)
     gas_vel[i][1]=float_type(0)

IC = h5py.File('IC.hdf5','w')
header = IC.create_group('header')
part0= IC.create_group('PartType0')

header.attrs.create('Boxsize',box_size)
part0.create_dataset('ParticleIDs', data=np.arange(0,gas_part_num))
part0.create_dataset('Coordinates', data=gas_coords)
part0.create_dataset('Velocites', data=gas_vel)
part0.create_dataset('masses', data=gas_masses)
IC.close()