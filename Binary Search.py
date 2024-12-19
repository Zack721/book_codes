List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
MaxItems = len(List)

SearchItem = 3

Found = False
SearchFailed = False
First = 0
Last = MaxItems - 1 #set boundaries of search area
#loop = 0
while Found == False and SearchFailed == False:
    #loop +=1
    Middle = (First + Last) // 2
    if List[Middle] == SearchItem:
        Found =True
    else:
        if First >= Last:
            SearchFailed = True
        else:
            if List[Middle] > SearchItem:
                Last = Middle - 1
            else:
                First = Middle + 1


if Found == True:
    print(Middle)
else:
    print("Item not present in list")

#print(f"Looped this many times{loop}")
