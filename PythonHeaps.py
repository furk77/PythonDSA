# Min heap (parent >= left and right) aka priority queues
import heapq  # heap queue library
arr = [10, 2, -34, 100, 89, -4]

heapq.heapify(arr) # heapify the array [turns it into a min-heap]

print(arr)

# Insert elements into the heap O(logn) time

heapq.heappush(arr, 34) # push elements into the heap (adds the element and heapifies it)

print(arr)

# pop an element from the heap (the minimum element) O(logn) time

heapq.heappop(arr) # pops the root and heapifies the array after
print(arr)

# Heap sort uses the min-max root property of the heaps to sort the elements
# In every iteration, it pops the root from the heap and appends it to the sorted list O(nlogn) time
# For min heap, this would result in an ascending order of elements
# For max heap, this would result in a descending order of elements
def heapSort(arr):
    heapq.heapify(arr)
    heap = []
    for i in range(len(arr)):
        heap.append(heapq.heappop(arr))
    return heap

print(heapSort([76, 21, -7, 555, 9]))

# Push an element into the heap while removing the root
min_element = heapq.heappushpop(arr, 81)

print(min_element, arr)

# Peak at the min-max element O(1) time

print(arr, arr[0])

# Max heap is not supported by heapq lib
# Negate all the numbers and then heapifiy it to get a negative max heap

arr2 = [10, -43, 123, -4, 43, 2332, -33]
arr2 = [-x for x in arr2]
heapq.heapify(arr2)
print(arr2)

# Get the max element (root)
max_element = -arr2[0]
print(max_element)

# When pushing an element into the max heap, negate it first

heapq.heappush(arr2, -22)

print(arr2)

# Build heap from scratch - Time: O(n log n)

C = [-5, 4, 2, 1, 7, 0, 3]

hp = []

for x in C:
  heapq.heappush(hp, x) # Push an element and then heapify it
  print(hp, len(hp)) # Check size of heap

# Putting tuples of items on the heap

D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

counter = Counter(D)

print(counter)

heap = []

for k, v in counter.items():
  heapq.heappush(heap, (v, k)) # heapify them according to their values (counts)

print(heap)
