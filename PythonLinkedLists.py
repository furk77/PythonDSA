# SinglyLinkedList Class Definition
class SinglyLinkedList:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    return str(self.val)

# Node Creation and Assignment
head = SinglyLinkedList(1)
A = SinglyLinkedList(2)
B = SinglyLinkedList(3)
C = SinglyLinkedList(4)

head.next = A
A.next = B
B.next = C

# Display Every Single Node
def printNodes(head):
  temp = head
  while temp != None:
    print(temp.val)
    temp = temp.next

printNodes(head)

# Alternate display linked list - O(n)
def display(head):
  curr = head
  elements = []
  while curr:
    elements.append(str(curr.val))
    curr = curr.next
  print(' -> '.join(elements))

#display(Head)

# See if a node exists in the list
def searchNode(head, target):
  temp = head
  while temp != None:
    if temp.val == target:
      return temp
    temp = temp.next

  return None

result = searchNode(head, 1)

if result:
  print("Success! The node was found!")
else:
  print("Failure! The node was not found.")

# Inserting a node at the beginning
def insertNodeBeg(head, node):
  newnode = node
  newnode.next = head
  head = newnode
  return head

head = insertNodeBeg(head, SinglyLinkedList(0))
printNodes(head)

# DoublyLinkedList class definition
class DoublyLinkedList:
  def __init__(self, val, next=None, prev=None):
    self.val = val
    self.next = next
    self.prev = prev

  def __str__(self):
    return str(self.val)
  

# Node Creation and Assignment
Head = Tail = DoublyLinkedList(1)

# Display the nodes regularly
def displayNodes(head):
  temp = head
  while temp != None:
    print(temp.val)
    temp = temp.next

# Display the nodes with an array
def displayarrNodes(head):
  temp = head
  values = []
  while temp != None:
    values.append(str(temp.val))
    temp = temp.next
  print(' <-> '.join(values))

#displayNodes(Head)
displayarrNodes(Head)

# Insert at the beginning
def insert_at_beg(head, node):
  if head is None:
    return node
  node.next = head
  head.prev = node
  return node

Head = insert_at_beg(Head, DoublyLinkedList(0))
displayarrNodes(Head)

# Insert at the end
def insert_at_end(head, node):
  if head is None:
    return node
  temp = head
  while temp.next != None:
    temp = temp.next
  temp.next = node
  node.prev = temp
  return head

Head = insert_at_end(Head, DoublyLinkedList(2))
displayarrNodes(Head)

# Search for a node in the list
def searchNode(head, target):
  temp = head
  while temp is not None:
    if temp.val is target:
      return True
    temp = temp.next

  return False

result = searchNode(Head, 0)

if result:
  print("Success! The node was found!")
else:
  print("Failure! The node was not found.")

