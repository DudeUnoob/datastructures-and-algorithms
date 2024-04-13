#Time Complexity O(n^2)

array = [2,4,5,3,7,8,1,5,10,4,6]

n = len(array)
print()
for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if array[j] < array[min_index]:
            min_index = j
    min_value = array.pop(min_index)
    array.insert(i, min_value)

print(array)



#Improvement to to the algorithm above


for i in range(n - 1):
    min_index = 1
    for j in range(i + 1, n):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
    