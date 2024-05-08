import numpy as np
import matplotlib.pyplot as plt
import control as con

z = con.TransferFunction.z

numerator = [2, 1]
denominator = [-1, 1]

frequencies = np.linspace(0, np.pi)

system = con.tf(numerator, denominator)
out = con.bode_plot(system)
plt.plot(out)
plt.show()