from read import *
from write import *

def convertToBytes(data):
    a_byte_array = bytearray(data, "utf8")

    byte_list = []

    for byte in a_byte_array:
        binary_representation = bin(byte)
        byte_list.append(binary_representation.replace("b",""))

    return byte_list
    

def convertToString(data):
    string = ""
    for i in data:
        string += chr(int(i,2))
    return string

print("Enter data:")
data = input()
dataBites = convertToBytes(data)
x = len(dataBites)
size = None
if x > 42:
    print("Error too much data (more than 42 bites)")
elif x > 31:
    size = 20
elif x > 24:
    size = 18
elif x > 17:
    size = 16
elif x > 12:
    size = 14
elif x > 7:
    size = 12
else:
    size = 10

if size:
    generate(size, dataBites, "", data)