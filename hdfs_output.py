import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom
import h5py

phi = np.linspace(0, 2*np.pi, 100)
R = 1
array_x = R * np.cos(phi)
array_y = R * np.sin(phi)

spline_coords, figure_spline_part = interpolate.splprep([array_x, array_y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_numper_per_side = 100
x_pictures_limits = [-1.0, 1.0]
y_pictures_limits = [-1.0, 1.0]

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
