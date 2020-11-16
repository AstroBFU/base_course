import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


# defining a variable value

seconds_in_year = 365*24*3600
seconds_in_day = 24*3600
years = 10

t = np.arange(0, seconds_in_year, seconds_in_day)

# define a function for a system of difequations

def danya_gravition_func (z,t):
    (x_merc, v_x_merc, y_merc, v_y_merc,
     x_ven, v_x_ven, y_ven, v_y_ven,
     x_ears, v_x_ears, y_ears, v_y_ears,
     x_mars, v_x_mars, y_mars, v_y_mars,
     x_Jupiter, v_x_Jupiter, y_Jupiter, v_y_Jupiter,
     x_Saturn, v_x_Saturn, y_Saturn, v_y_Saturn,
     x_Uranus , v_x_Uranus , y_Uranus , v_y_Uranus,
     x_Neptune, v_x_Neptune, y_Neptune, v_y_Neptune
     ) = z
    
    dxdt_merc = v_x_merc
    dv_xdt_merc = -G *sun_mass * merc_mass / (x_merc**2 +y_merc**2)**1.5
    dydt_merc = v_y_merc
    dv_ydt_merc = -G *sun_mass * merc_mass / (x_merc**2 +y_merc**2)**1.5
    
    dxdt_ven = v_x_ven
    dv_xdt_ven = -G *sun_mass * ven_mass / (x_ven**2 +y_ven**2)**1.5
    dydt_ven = v_y_ven
    dv_ydt_ven = -G *sun_mass * ven_mass / (x_ven**2 +y_ven**2)**1.5
    
    dxdt_ears = v_x_ears
    dv_xdt_ears = -G *sun_mass * ears_mass / (x_ears**2 +y_ears**2)**1.5
    dydt_ears = v_y_ears
    dv_ydt_ears = -G *sun_mass * ears_mass / (x_ears**2 +y_ears**2)**1.5
    
    dxdt_mars = v_x_mars
    dv_xdt_mars = -G *sun_mass * mars_mass / (x_mars**2 +y_mars**2)**1.5
    dydt_mars = v_y_mars
    dv_ydt_mars = -G *sun_mass * mars_mass / (x_mars**2 +y_mars**2)**1.5
    
    dxdt_Jupiter = v_x_Jupiter
    dv_xdt_Jupiter = -G *sun_mass * Jupiter_mass / (x_Jupiter**2 +y_Jupiter**2)**1.5
    dydt_Jupiter = v_y_Jupiter
    dv_ydt_Jupiter = -G *sun_mass * Jupiter_mass / (x_Jupiter**2 +y_Jupiter**2)**1.5
    
    dxdt_Saturn = v_x_Saturn
    dv_xdt_Saturn = -G *sun_mass * Saturn_mass / (x_Saturn**2 +y_Saturn**2)**1.5
    dydt_Saturn = v_y_Saturn
    dv_ydt_Saturn = -G *sun_mass * Saturn_mass / (x_Saturn**2 +y_Saturn**2)**1.5
    
    dxdt_Uranus = v_x_Uranus
    dv_xdt_Uranus = -G *sun_mass * Uranus_mass / (x_Uranus**2 +y_Uranus**2)**1.5
    dydt_Uranus = v_y_Uranus
    dv_ydt_Uranus = -G *sun_mass * Uranus_mass / (x_Uranus**2 +y_Uranus**2)**1.5
    
    dxdt_Neptune = v_x_Neptune
    dv_xdt_Neptune = -G *sun_mass * Neptune_mass / (x_Neptune**2 +y_Neptune**2)**1.5
    dydt_Neptune= v_y_Neptune
    dv_ydt_Neptune = -G *sun_mass * Neptune_mass / (x_Neptune**2 +y_Neptune**2)**1.5
    
    return(
           dxdt_merc, dv_xdt_merc, dydt_merc, dv_ydt_merc,
           dxdt_ven, dv_xdt_ven, dydt_ven, dv_ydt_ven,
           dxdt_ears, dv_xdt_ears, dydt_ears, dv_ydt_ears,
           dxdt_mars, dv_xdt_mars, dydt_mars, dv_ydt_mars,
           dxdt_Jupiter, dv_xdt_Jupiter, dydt_Jupiter, dv_ydt_Jupiter,
           dxdt_Saturn, dv_xdt_Saturn, dydt_Saturn, dv_ydt_Saturn,
           dxdt_Uranus, dv_xdt_Uranus, dydt_Uranus, dv_ydt_Uranus,
           dxdt_Neptune, dv_xdt_Neptune, dydt_Neptune, dv_ydt_Neptune
           
           )

# defining the initial values
G = 6.67*10**(-11)
sun_mass = 1.989*10**30
ae = 1.496*10**11
  
x0_merc = 0
v_x0_merc = -46994.467
y0_merc = 0.38*ae
v_y0_merc = 0
merc_mass = 3.302*10**23

x0_ven = 0
v_x0_ven = -34859.98
y0_ven = 0.72*ae
v_y0_ven = 0
ven_mass = 4.869*10**24

x0_ears = 0
v_x0_ears = -29784.862
y0_ears = ae
v_y0_ears = 0
ears_mass = 5.974*10**24

x0_mars = 0
v_x0_mars = -24129.765
y0_mars = 1.5237*ae
v_y0_mars = 0
mars_mass = 6.419*10**23

x0_Jupiter = 0
v_x0_Jupiter = -13066.229
y0_Jupiter = 5.2*ae
v_y0_Jupiter = 0
Jupiter_mass = 1.899*10**27

x0_Saturn = 0
v_x0_Saturn = -9642.607
y0_Saturn = 9.5*ae
v_y0_Saturn = 0
Saturn_mass = 4.685*10**26

x0_Uranus = 0
v_x0_Uranus = -6808.855998
y0_Uranus = 19.19*ae
v_y0_Uranus = 0
Uranus_mass = 8.683*10**25

x0_Neptune = 0
v_x0_Neptune = -5437.045626
y0_Neptune = 30.06*ae
v_y0_Neptune = 0
Neptune_mass = 1.024*10**26

z0 = (x0_merc,    v_x0_merc,    y0_merc,    v_y0_merc,
      x0_ven,     v_x0_ven,     y0_ven,     v_y0_ven,
      x0_ears,    v_x0_ears,    y0_ears,    v_y0_ears,
      x0_mars,    v_x0_mars,    y0_mars,    v_y0_mars,
      x0_Jupiter, v_x0_Jupiter, y0_Jupiter, v_y0_Jupiter,
      x0_Saturn,  v_x0_Saturn,  y0_Saturn,  v_y0_Saturn,
      x0_Uranus,  v_x0_Uranus,  y0_Uranus,  v_y0_Uranus,
      x0_Neptune, v_x0_Neptune, y0_Neptune, v_y0_Neptune
      )

# solving a system of dif equations

sol = odeint(danya_gravition_func,z0,t)

# building a solution as a graph and animating it

fig = plt.figure()
planets = []

for i in range(0, len(t), 1):
    sun, = plt.plot([0], [0],'black', ms=10)
    
    merc, = plt.plot(sol[:i,0], sol[:i,2],'r-')
    merc_line, = plt.plot(sol[i,0], sol[i,2],'ro')
    
    ven, = plt.plot(sol[:i,4], sol[:i,6],'darkorange-')
    ven_line, = plt.plot(sol[i,4], sol[i,6],'darkorangeo')
    
    ears, = plt.plot(sol[:i,8], sol[:i,10],'greenyellow-')
    ears_line, = plt.plot(sol[i,8], sol[i,10],'greenyellowo')
    
    mars, = plt.plot(sol[:i,12], sol[:i,14],'aqua-')
    mars_line, = plt.plot(sol[i,12], sol[i,14],'aquao')
    
    Jupiter, = plt.plot(sol[:i,16], sol[:i,18],'slategray-')
    Jupiter_line, = plt.plot(sol[i,16], sol[i,18],'slategrayo')
    
    Saturn, = plt.plot(sol[:i,20], sol[:i,22],'royalblue-')
    Saturn_line, = plt.plot(sol[i,20], sol[i,22],'royalblueo')
    
    Uranus, = plt.plot(sol[:i,24], sol[:i,26],'navy-')
    Uranus_line, = plt.plot(sol[i,24], sol[i,26],'navyo')
    
    Neptune, = plt.plot(sol[:i,28], sol[:i,30],'magenta-')
    Neptune_line, = plt.plot(sol[i,28], sol[i,30],'magentao')
    
    planets.append([sun, merc, merc_line, ven, ven_line, ears, ears_line, mars, mars_line, 
Jupiter, Jupiter_line, Saturn, Saturn_line, Uranus, Uranus_line, Neptune, Neptune_line])
    
ani = ArtistAnimation(fig, planets,interval=50)
plt.axis('equal')
ani.save('laba_12_gif')
    
    
    
    
    
    