import os

def CreateFile(file_name): 
    f = open(file_name, "xt")
    size_file = os.path.getsize(file_name)
    #print(f" created file is{size_file}bytes")

def AppendFile(file_name, message):
    f = open(file_name, "at")
    f.write(message)
    f.close()

def SizeOfFile(file_name):
    size_file = os.path.getsize(file_name)
    print(f"current size:{size_file}bytes")

def KeepCharacters(file_name, start, end):
    f = open(file_name, "rt")
    contents = f.read()
    f.close()

    f= open(file_name, "wt")
    if end == None:
        contents = contents[0:start]
        f.write(contents)
        f.close()
    else:
        contents = contents[0:start] + contents[end:]
        f.write(contents)
        f.close()

def PrintContents(file_name):
    f = open(file_name, "rt")
    print(f.read())
    f.close()

def DeleteFile(file_name):
    os.remove(file_name)



if __name__ == "__main__":
    file_name = "binary.dat"
    """CreateFile(file_name)
    print("\n")"""
    DeleteFile(file_name)
    
    """SizeOfFile(file_name)"""
    """ 
   print("10 chracters")
    SizeOfFile(file_name)
    print("\n")

    KeepCharacters(file_name, 8, None)
    print("8 charcters")
    PrintContents(file_name)
    SizeOfFile(file_name)
"""

