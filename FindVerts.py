import struct

def isInRange(x):
    return abs(x) > 0.01 and abs(x) < 1000

path = "Geometry.bin"

with open(path, 'rb') as f:
    data = f.read()

#don't read more than 100kb of data, so this thing in't spitting out text forever.
dataLen = min(100 * 1024, len(data))

for index in range(0, dataLen - 8, 4):
    x = struct.unpack('f', data[index+0:index+4])[0]
    y = struct.unpack('f', data[index+4:index+8])[0]
    z = struct.unpack('f', data[index+8:index+12])[0]

    if isInRange(x) and isInRange(y) and isInRange(z):
        print('({}, {}, {}) @ {:X}'.format(x, y, z, index))
