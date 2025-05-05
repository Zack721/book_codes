def CreateFile(file_name):
    f = open(file_name, "x")
    print(f"file {file_name} was created")


def ReadTextFile(file_name):
    file = open(file_name, "rt")
    print(file.read())
    file.close()

def GetFirstLine(file_name):
    f = open(file_name, "rt")
    for line in f:
        print(line[0:2])
        return

def  CreateListOfWords(file_name):
    f = open(file_name, "rt")
    list_of_char = []
    
    for line in f:
        string = str()
        for character in line:
            if character == " " or character == "\t" or character == "\n":
                list_of_char.append(string)
                print("sean diddy")
                string += character
                string = ""
                continue
            string += character
    list_of_char.append(string)
    for i in list_of_char:
        print(i)
    

def WriteToFile(file_name, text):
    file = open(file_name, "wt")
    file.write(text)
    file.close()

if __name__ == "__main__":
    file_name = "new_file1.txt"
    """ReadTextFile(file_name)
    WriteToFile(file_name, "My name a ISaac")"""
    #GetFirstLine(file_name)
    CreateListOfWords(file_name)