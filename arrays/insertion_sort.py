#Time Complexity O(n^2)
array = [2,4,5,3,7,8,1,5,10,4,6]

n = len(array)
for i in range(1,n):
    insert_index = i
    current_value = array.pop(i)
    for j in range(i-1, -1, -1):
        if array[j] > current_value:
            insert_index = j
    array.insert(insert_index, current_value)

print("Sorted array:", array)