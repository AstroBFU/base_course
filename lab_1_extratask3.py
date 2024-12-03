import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

G = 6.67 * 10**(-11)
M_son = 1.989 * 10**30
L_son = 3.827 * 10**26
R = 6400 * 10**3
q = 147 * 10**9
v_q = 30.4 * 10**3

e = (v_q**2 * q)/(G*M_son) - 1
p = q *(1+e)
a = q / (1-e)
T = np.sqrt((4*np.pi**2 * a**3)/(G*M_son))

t = np.arange(0, T, 1000)

def enrgy_func(z, t):
    phi, E = z

    r = p / (1 + e*np.cos(phi))

    dphi_dt = np.sqrt(G*M_son*p) / r**2

    dE_dt = (L_son * R**2)/(4*r**2)

    return dphi_dt, dE_dt

phi_0 = 0
E_0 = 0
z_0 = phi_0, E_0

E_t = odeint(enrgy_func, z_0, t)

plt.plot(t/3600, E_t[:,1], label="Энергия")
plt.xlabel("Время, часы")
plt.ylabel("Энергия, Дж")
plt.title("Закон изменения энергии")
plt.legend()

plt.savefig("lab_extratask3.png")

E_sum = round(E_t[-1,-1] / 10**25, 2) * 10**25

print("Энергия, которую планета получила за лдин оборот равна:", E_sum, "Дж")
