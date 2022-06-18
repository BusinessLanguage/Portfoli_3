import struct
import math

input1 = input("Enter int decimal number here: ")
input2 = input ("Enter float decimal number here: ")

input1_pack = struct.pack('h', int(input1))
input2_pack = struct.pack('f', float(input2))

print(input1_pack)
print(input2_pack)

input1_unpack = struct.unpack('h', input1_pack)
input2_unpack = struct.unpack('f', input2_pack)

print(input1_unpack)
print(input2_unpack)

assert int(input1) == input1_unpack[0]
assert math.fabs(float(input2) - input2_unpack[0]) < 0.000001
