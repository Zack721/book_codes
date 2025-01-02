import random

def LinearSearch(container, item_to_find):  #container = array
    index_of_element = 0
    for i in container:
        
        if i == item_to_find:
            return index_of_element
        index_of_element +=1

    return -1
def TestingLinearSearch():
    array = []

    for i in range(0,100):
        array.append(random.randint(0, 1000))

    array[50] = 131
    
    #print(f"item found and it was the {where_item_was} element in the array")
    assert LinearSearch(array, 131) <= 50
    array[77] == 1234
    assert LinearSearch(array, 1234) <= 77
if __name__ == "__main__":
    TestingLinearSearch()
    print("Success")
   