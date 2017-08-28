import struct
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

path = "Geometry1.bin"
maxDimLen = 3.0; #only a valid vertex if it's within 3 units of the origin on each exis
maxFileReadLen = 4 * 1024*1024 #4MB

def isInRange(x):
    return abs(x) < maxDimLen

with open(path, 'rb') as f:
    data = f.read()

readLen = min(len(data)-36, maxFileReadLen)

xs = []
ys = []
zs = []
for offset in range(0, readLen, 4):
    ptData = struct.unpack('ffffffiff', data[offset+0:offset+36])
    x = ptData[0]
    y = ptData[1]
    z = ptData[2]
    nx = ptData[3]
    ny = ptData[4]
    nz = ptData[5]
    unkn = ptData[6]
    u = ptData[7]
    v = ptData[8]

    mag = nx*nx + ny*ny + nz*nz

    if isInRange(x) and isInRange(y) and isInRange(z) and mag > 0.999 and mag < 1.001 \
        and u > -0.01 and u < 1.01 and v > -0.01 and v < 1.01:
            xs.append(x)
            ys.append(y)
            zs.append(z)

fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(xs, ys, zs)
ax.set_xlim(-maxDimLen, maxDimLen)
ax.set_ylim(-maxDimLen, maxDimLen)
ax.set_zlim(-maxDimLen, maxDimLen)
plt.show()


