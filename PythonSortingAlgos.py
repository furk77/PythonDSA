# Bubble sort O(n^2) time
# Compares i and i-1 continiously and swaps them if needed
# If no swaps were performed, exit the function the array is sorted

def bubbleSort(arr):

  done = False

  while not done:
    done = True
    for i in range(1, len(arr)):
      if arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        done = False

  return arr

A = [0, -32, 132, 34, -3, 12, 222]

print(bubbleSort(A))

# Insertion sort O(n^2) time

def insertionSort(arr):
    for i in range(1, len(arr)):
      for j in range(i, 0, -1):
        if arr[j-1] > arr[j]:
          arr[j-1], arr[j] = arr[j], arr[j-1]
        else:
          break
    return arr

B = [0, -32, 132, 34, -3, 12, 222]

print(insertionSort(B))

# Selection sort O(n^2) time

def selectionSort(arr):
    for i in range(len(arr)):
      min_index = i
      for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
          min_index = j
      arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

C = [0, -32, 132, 34, -3, 12, 222]

print(selectionSort(C))

# Counting Sort
# Time: O(n + k) where k is the range of data

# Note - This can be written with negative arrays, but we'll stick to positive arrays,
# so k is the max of the array

# Space: O(k)
def countingSort(arr):
    maxValue = max(arr)
    count = [0] * (maxValue + 1)

    for i in range(len(arr)):
        num = arr.pop()
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

D = [0, 23, 1, 323, 88, 12]

countingSort(D)

# Merge Sort
# Time: O(n log n)
# Space: O(n) - Note: can be Log n, but this is harder to write


D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def merge_sort(arr):
  n = len(arr)

  if n == 1:
    return arr

  m = len(arr) // 2
  L = arr[:m]
  R = arr[m:]

  L = merge_sort(L)
  R = merge_sort(R)
  l, r = 0, 0
  L_len = len(L)
  R_len = len(R)

  sorted_arr = [0] * n
  i = 0

  while l < L_len and r < R_len:
    if L[l] < R[r]:
      sorted_arr[i] = L[l]
      l += 1
    else:
      sorted_arr[i] = R[r]
      r += 1

    i += 1

  while l < L_len:
    sorted_arr[i] = L[l]
    l += 1
    i += 1

  while r < R_len:
    sorted_arr[i] = R[r]
    r += 1
    i += 1

  return sorted_arr

merge_sort(D)

# Quick Sort
# Time: O(n log n) (Average case, technically Worst case is O(n^2))
# Space: O(n)

E = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def quick_sort(arr):
  if len(arr) <= 1:
    return arr

  p = arr[-1]

  L = [x for x in arr[:-1] if x <= p]
  R = [x for x in arr[:-1] if x > p]

  L = quick_sort(L)
  R = quick_sort(R)

  return L + [p] + R

quick_sort(E)

# Python built-in sorting

F = [-5, 3, 2, 1, -3, -3, 7, 87, 2]

F.sort() # Modifies the original array
print(F)

F.sort(reverse = True) # sort in descending order
print(F)

G = [-5, 3, 2, 1, -3, -3, 7, 87, 2]

print(sorted(G), G) # Does not modify the original array, returns a new list

# Sort array of tuples

I = [(-5, 3), (2, 1), (-3, -3), (7, 2), (2, 2)]

sorted_I = sorted(I, key = lambda t: t[0]) # sort the list of tuples by the first value of the tuples (in ascending order)

print(sorted_I)
