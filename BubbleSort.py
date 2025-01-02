array = [42, 52, 10, 2, 20, 29, 82, 16, 15, 56]

n = len(array)

for i in range(n):
    #swapped = False
    print("I AM HERE")
    for j in range(0, n-1):
        
        if array[j] > array[j+1]:
            #swapped  = True
            temp = array[j+1]
            array[j+1]= array[j]
            array[j]  = temp

            print(f"{array[j]}swapped places with{array[j+1]}")
    #if not swapped:
        #break

print(array)
            
            