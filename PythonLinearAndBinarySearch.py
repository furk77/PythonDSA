# Linear Search
def linearSearch(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

arr = [10,20,30,40]

if linearSearch(arr, 40):
    print("Found")
else:
    print("Not Found")

# Binary Search
def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + ((right - left) // 2) # to prevent int overflow
        if arr[mid] == target:
          return True
        elif arr[mid] > target:
          right = mid -1
        else:
          left = mid + 1
    return False


if binarySearch(arr, 20):
    print("Found")
else:
    print("Not Found")
