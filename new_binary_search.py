def BinarySearch(search_item):
    array = [1,3,5,7,9]
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

assert BinarySearch(7) == 3
assert BinarySearch(5) == 2
assert BinarySearch(6) == True
assert BinarySearch(1) == 0
assert BinarySearch(10) == True
assert BinarySearch(0) == True
