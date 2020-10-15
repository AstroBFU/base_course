from lab3_1 import gravity_constant as G
from lab3_1 import a
from lab3_1 import h
from lab3_1 import b
from lab3_base import uskorenie_svobodnogo_padenya as g
import numpy as np

v=np.sqrt((g*h*np.tan(b)**2)/((2*np.cos(b)**2)*(1-np.tan(b)*np.tan(a))))

print(v)
