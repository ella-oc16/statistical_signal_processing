import matplotlib.pyplot as plt
import numpy as np


def function(x, a_0):
    return a_0*x - (1.5*a_0 - 2)*x**2 - (1-0.5*a_0)*x**4

a_0 = 0
etas = np.linspace(0, 1)
velocities = []

for eta in etas:
    velocities.append(function(eta,a_0=a_0))

plt.plot(etas, velocities)
plt.xlabel('η')
plt.ylabel('u/U')
plt.title(f'a_0 = {a_0}')
plt.show()

