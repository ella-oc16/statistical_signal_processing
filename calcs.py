import numpy as np
import matplotlib.pyplot as plt

# pitot pressure in Pa
p = 0.43 * 100
density = 1.225
v = 14.64 *1e-6       # dynamic visocity (from databook)

def RE(p):
    U = np.sqrt((2*p)/density)
    return (1.14*U)/v


freestream_velocity = np.sqrt((2*p)/density)        # Bernoulli


u_bars = [5.371599952, 5.621411072, 5.73561087, 5.878348762, 6.070247006, 6.125785642, 6.243450998, 6.311319942, 6.497452224, 6.59617154, 6.669357637, 6.946092516, 7.196010036, 7.404370566,
7.483082838,
7.735289939,
7.917291118,
8.242290426,
8.520648855,
8.634337234,
8.724587476,
8.794418498]
y = [0.5,0.75,1,1.25,1.5,1.75,2,2.5,3,3.5,4,5,6,7,8,9,10,12,14,16,18,20,]
u_dashes = [0.488865253,
0.521786425,
0.85629621,
0.464589959,
0.653985055,
0.507457155,
0.58671048,
0.455470891,
0.437479765,
0.595739064,
0.445900249,
0.397313848,
0.381778261,
0.481237808,
0.378925863,
0.385290161,
0.359422572,
0.200090114,
0.231895779,
0.138320761,
0.112368569,
0.072444962]


# interpolating between the cf = 0.004 and 0.006 lines, cf is approx. 0.0047
friction_vel = np.sqrt((0.5*0.0047*(freestream_velocity**2)))
sq_fric_vel = friction_vel**2

res = []
for i in range(len(u_dashes)):
    x = (u_dashes[i]**2)/(u_bars[i]**2)
    res.append(np.sqrt(x))

plt.plot(y, res, color='green')
plt.title(f"Ratio of Mean of Squared Fluctation Velocity to Squared Mean Velocity")
plt.xlabel('y (mm)')
plt.ylabel("Ratio")
plt.show()





"""
us = []
for u in u_bars:
    us.append(u/freestream_velocity)


plt.plot(us, y, color='red')
plt.title(f'Boundary Layer Velocity Profile (free-stream velocity = {np.round(freestream_velocity, 2)} m/s')
plt.ylabel('y (mm)')
plt.xlabel('u/U')
plt.show()
"""
