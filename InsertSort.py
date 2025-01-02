def InsertSort(array):
    for i in range(1, len(array)):
        current = array[i]  #42
        compared = i - 1 # index of 52

        while compared >= 0 and array[compared] > current:
            array[compared + 1] = array[compared]       # 52 is 1 and 2 element
            compared -= 1

        array[compared + 1] = current 
    
    return array

def ChatgptInsertsort(arr):
    for i in range(1, len(arr)):
        current = arr[i]  
        j = i - 1    

        while j >= 0 and arr[j] > current:
            arr[j + 1] = arr[j]  
            j -= 1

        arr[j + 1] = current

    return arr

if __name__ == "__main__":
    
    array = [52,42, 10, 2, 20, 29, 82, 16, 15, 56]
    print(f"pre chang array: {array}")
    InsertSort(array)
    print(array)

