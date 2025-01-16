# Fibonacci Recursion F(n) = f(n-1) + f(n-2)

def fib(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fib(n-1) + fib(n-2)

print(fib(10))

# LinkedList Recursion

class SinglyLinkedList:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return self.value

head = SinglyLinkedList("a")
b = SinglyLinkedList("b")
c = SinglyLinkedList("c")
d = SinglyLinkedList("d")

head.next = b
b.next = c
c.next = d

# Print nodes recursively in reverse (LIFO-style)
def printNodesRecursively(node):
  if not node:
    return

  printNodesRecursively(node.next)
  print(node.value)

printNodesRecursively(head)

# Print nodes recursively (FIFO-style)
def printNodesRecursively(node):
  if not node:
    return

  print(node.value)
  printNodesRecursively(node.next)


printNodesRecursively(head)
