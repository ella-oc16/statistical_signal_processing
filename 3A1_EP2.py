import numpy as np


# r1, r2, ro are all 3D vectors, they are dimensionless position vectors

# rv is unit vector in direction of line from r1 to r2
r1 = np.array([0.0001, 5, 0])
r2 = np.array([0.0001, 7, 0])
r0 = np.array([0, 0, 0])

def linev(r1, r2, ro):
    ra = r1-ro
    rahat = ra/np.linalg.norm(ra)
    rb = r2-ro
    rbhat = rb/np.linalg.norm(rb)
    
    rv = r2-r1
    rvhat = rv/np.linalg.norm(rv)

    raxrvh = np.cross(ra, rvhat)

    v = (0.25/np.pi) * np.dot(rvhat, rbhat-rahat) * raxrvh/(np.linalg.norm(raxrvh))**2
    return v

def seminfv(r1, ro):
   ra = r1-ro
   rahat = ra/np.linalg.norm(ra)
   rbhat = np.array([1,0,0])
   rvhat = np.array([1,0,0])

   raxrvh = np.cross(ra, rvhat)
   v = (0.25/np.pi) * np.dot(rvhat, rbhat-rahat) * raxrvh/(np.linalg.norm(raxrvh))**2
   return v

def hsv(r1, r2, ro):
    vleg1 = -seminfv(r1,ro)
    vhead = linev(r1,r2,ro)
    vleg2 = seminfv(r2,ro)
    velhs = vleg1 + vhead + vleg2
    return velhs

v = hsv(r1, r2, r0)
print(v)
