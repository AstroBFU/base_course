import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(-5, 5, 0.1)

def div(pup ,t)
y, x = pup

dydt = x
dxdt = np.sin(x) + np.cos(x)

return dydt, dxdt

