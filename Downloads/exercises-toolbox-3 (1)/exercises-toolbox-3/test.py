from uncertainties import ufloat
import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
import sympy

x,y,z = sympy.var('x y z')

f= 3*x+ 7*x**2*z- sympy.cos(x)
print(f.diff(x))