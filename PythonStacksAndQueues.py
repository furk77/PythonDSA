# Creating a stack as a list

stack = []

print(stack)

# adding elements to the stack with append
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)

# removing elements from the stack with pop
stack.pop()
print(stack)

# Get the size of the stack
print(len(stack))

# peek at the top element of the stack
print(stack[-1])
# or
print(stack[len(stack) - 1])

# check if the stack is empty
print("Stack is not empty") if stack else print("Stack is empty")

# Creating a queue with the deque class
from collections import deque

queue = deque()

print(queue)

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print(queue)

# Removing elements from the queue
queue.popleft()

print(queue)

# Getting the size of a queue
print(len(queue))

# Read the first element in the queue
print(queue[0])
# Read the last element in the queue
print(queue[-1])

