def BookBinarySearch(search_item, list):
    n = len(list)
    found = False
    search_failed = False
    first = 0
    last = n - 1

    while found == False and search_failed == False:  #so basically these are the entry conditions
        Mid = (first + last) // 2  
        #print(Mid)
        if list[Mid] == search_item:
            found = True    

        else:
            if first >= last:
                search_failed = True #true if not in list
            
            else:
                if list[Mid] > search_item:
                    last = Mid - 1 #changes the previous mid -1 the new upper boundary
                else:
                    first = Mid + 1 # item is in bigger half so lower boundary is new mid
    
def BinarySearch(search_item, array):
    first =0
    last = len(array) - 1

    while  first > last:
        mid = (first + last) //2
        if search_item < array[mid]:
            last = mid -1 
        elif search_item > array[mid]:
            first = mid +1
            
        else: 
            return mid
            
    return False

if __name__ == "__main__":
    import InsertSort

    list = InsertSort.InsertSort([52,42, 10, 2, 20, 29, 82, 16, 15, 56])
    assert BookBinarySearch(16, list) == 3
    assert BinarySearch(16, list) == 3



