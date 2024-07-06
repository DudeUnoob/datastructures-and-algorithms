
#Time Complexity O(n^2)
array = [2,4,5,3,7,8,1,5,10,4,6]


for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]


 

for i in range(len(array)):
    swapped = False
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            array[j], array[j+1] = array[j+1], array[j]
            swapped = True

    if swapped == False:
        break

    

print(array)



