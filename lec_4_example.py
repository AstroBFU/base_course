import numpy as np

def grav_accel(phi=0, h=0):
  '''ускорение свободного падения,
  phi - широта места наблюдения
  h - высота на поверхностью Земли
  '''
  g=9.7803*(1+0.05*(np.sin(phi))**2-0.000006*(np.sin(2*phi))**2)-0.0000003086*h
  return g

def losing_weight_function(mass=50, phi_0=54,phi_eng=0,h_0=0, h_end=3000):
  '''Функция,определяющая вес
  '''
  p_0=grav_accel(phi_0, h_0)*mass
  delta_P = grav_accel(p_0-p_0)*100
  if delta_P > 0:
    print('Вы похудеете на: ', delta_P, 'гр.')
  elif delta_P < 0:
    print('Вы поправитесь на: ', delta_P*(-1), 'гр.')
  else:
    print('Вы жиртрес!')

losing_weight_function(70,8,1000,54,0)