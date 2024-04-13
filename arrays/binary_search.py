#Time Complexity: O(log _2 n) or O(log n)

def binary_search(arr, target):
    arr.sort()
    low = 0
    high = len(arr) - 1
    
    for _ in range(len(arr)):
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1


array = [2, 4, 5, 3, 7, 8, 1, 5, 10, 4, 6]
target = 5
result = binary_search(array, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
