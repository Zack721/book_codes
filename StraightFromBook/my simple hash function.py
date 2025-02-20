user_input = input("Enter a single letter: ")
list = []
for i in user_input:
    list.append(i)


    
hash_output = 0

for letter in list:

    if letter == "a":
        hash_output += 1 
        hash_output *= hash_output
    elif letter == "b":
        hash_output += 2
        hash_output *= hash_output
    elif letter == "c":
        hash_output += 3
        hash_output *= hash_output
    elif letter == "d":
        hash_output += 4
        hash_output *= hash_output
    elif letter == "e":
        hash_output += 5
        hash_output *= hash_output
    elif letter == "f":
        hash_output += 6
        hash_output *= hash_output
    elif letter == "g":
        hash_output += 7
        hash_output *= hash_output
    elif letter == "h":
        hash_output += 8
        hash_output *= hash_output
    elif letter == "i":
        hash_output += 9
        hash_output *= hash_output
    elif letter == "j":
        hash_output += 10
        hash_output *= hash_output
    elif letter == "k":
        hash_output += 11
        hash_output *= hash_output
    elif letter == "l":
        hash_output += 12
        hash_output *= hash_output
    elif letter == "m":
        hash_output += 13
        hash_output *= hash_output
    elif letter == "n":
        hash_output += 14
        hash_output *= hash_output
    elif letter == "o":
        hash_output += 15
        hash_output *= hash_output
    elif letter == "p":
        hash_output += 16
        hash_output *= hash_output
    elif letter == "q":
        hash_output += 17
        hash_output *= hash_output
    elif letter == "r":
        hash_output += 18
        hash_output *= hash_output
    elif letter == "s":
        hash_output += 19
        hash_output *= hash_output
    elif letter == "t":
        hash_output += 20
        hash_output *= hash_output
    elif letter == "u":
        hash_output += 21
        hash_output *= hash_output
    elif letter == "v":
        hash_output += 22
        hash_output *= hash_output
    elif letter == "w":
        hash_output += 23
        hash_output *= hash_output
    elif letter == "x":
        hash_output += 24
        hash_output *= hash_output
    elif letter == "y":
        hash_output += 25
        hash_output *= hash_output
    elif letter == "z":
        hash_output += 26
        hash_output *= hash_output
    else:
        print("Invalid input. Please enter a single letter from A-Z.")

print(hash_output)