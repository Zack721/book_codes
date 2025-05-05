import os
import struct  

#copied part of lines 2 and 12

def CreateBinaryFile(file_name):
    f = open(file_name, "xb")
    f.close()

def WriteToFile(file_name):
    f = open(file_name, "wb")
    f.write(struct.pack('i', 0)) #cannot use old method directlt put integer
    f.close()
    

def ReadFile(file_name):
    f = open(file_name, "rb")
    variable = f.read
    print(variable)
    print(type(variable))
    f.close()

def GetSize(file_name):
    f = os.path.getsize(file_name)

if __name__ == "__main__":
    file_name = "BinaryTXTTest"
    CreateBinaryFile(file_name)
    WriteToFile(file_name)
    ReadFile(file_name)


    
