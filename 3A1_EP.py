import matplotlib.pyplot as plt
import numpy as np

constant = 0.2 / 2*np.pi

def v_dash(a):
    return constant * (4*a*np.log(np.abs((0.25-a)/a)) + ((1-a)/0.75)*np.log(np.abs((1-a)/(0.25-a))))

a_list = np.linspace(0.001,0.999)

y_s = []
for a in a_list:
    y_s.append(v_dash(a))

plt.plot(a_list, y_s)
plt.xlabel('x/c')
plt.ylabel('v/U @ y = 0')
plt.axhline(y=0, linestyle='dashed', color='gray')
#plt.show()

integral = np.trapz(y_s, a_list)
print(integral)
print(np.cumsum(y_s))