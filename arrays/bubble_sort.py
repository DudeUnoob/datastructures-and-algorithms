
#Time Complexity O(n^2)
array = [2,4,5,3,7,8,1,5,10,4,6]

n = len(array)

for i in range(n):
    for j in range(n - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]


print(array)




#We can optimize this algorithm even more by doing the following

for i in range(n):
    swapped = False
    for j in range(n - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swapped = True

    if swapped == False:
        break


print(array)
