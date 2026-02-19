import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

v = np.array([2,3])
s = np.array([0,3])

print(s)

vecs = np.array([v, s])

origins = np.zeros((2,2))

plt.figure(figsize=(6,6))

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.quiver(origins[:,0], origins[:,1],
           vecs[:,0], vecs[:,1],
           color=['red','blue'],
           angles='xy', scale_units='xy', scale=1)

plt.xlim(-5,5)
plt.ylim(-5,5)
plt.gca().set_aspect('equal')

plt.grid()
plt.title("Visualisasi Vektor v dan s")

plt.show()

z = v+s
print(z)

vecs = np.array([v, s, z])

origin = np.zeros((3,2))

plt.axis('equal')
plt.grid()
plt.ticklabel_format(style='sci', axis='both', scilimits=(0,0))

plt.quiver(origin[:,0], origin[:,1],
           vecs[:,0], vecs[:,1],
           color=['r','b','g'],
           angles='xy', scale_units='xy', scale=1)

plt.show()
