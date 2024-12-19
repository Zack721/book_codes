List = [53, 21, 60, 18, 42, 19]
for n in range(1, len(List)):
    ItemToBeInserted =List[n]  #21   
    CurrentItem = n - 1        #53 index
    while (List[CurrentItem] > ItemToBeInserted) and (CurrentItem > -1):     # while 53 > 21 and 0> -1  
        List[CurrentItem + 1] = List[CurrentItem]
        #print(List)
        CurrentItem -= 1

    List[CurrentItem + 1] = ItemToBeInserted
    #print(List[CurrentItem+1])
#print(List)