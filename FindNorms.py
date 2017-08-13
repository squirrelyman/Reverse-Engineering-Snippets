import struct

def isInRange(x):
    return abs(x) > 0.01 and abs(x) < 1000

path = "C:/Users/joehe/Documents/Visual Studio 2015/Projects/NFSLoader/NFS Hacks/Cars/A3/Geometry.bin"

with open(path, 'rb') as f:
    data = f.read()

#don't read more than 100kb of data, so this thing in't spitting out text forever.
dataLen = min(100 * 1024, len(data))

for index in range(0, dataLen - 8, 4):
    x = struct.unpack('f', data[index+0:index+4])[0]
    y = struct.unpack('f', data[index+4:index+8])[0]
    z = struct.unpack('f', data[index+8:index+12])[0]
    mag = x*x + y*y + z*z

    if mag > 0.9999 and mag < 1.0001:
        print('({}, {}, {}) @ {:X}'.format(x, y, z, index))
