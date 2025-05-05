def DeleteChar(start, num):
    f.seek(start)
    for i in range(num):
        f.write(" ")
if __name__ == "__main__":
    file_name = "textfile1.txt" 
    f = open(file_name, "wt")
    f.write("My name is Sir Isaac Ben Akan Taylor the First")
    DeleteChar(41, 4)

    