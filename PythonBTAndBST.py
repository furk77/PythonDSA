# Binary tree node class
class node:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.val)

# Node creation and assignment
root = node(1)
A = node(2)
B = node(3)
C = node(4)
D = node(5)
E = node(6)
F = node(7)

root.left = A
root.right = B
A.left = C
A.right = D
B.left = E
B.right = F

# DFS - preorder search (parent-left-right)
def preorderSearch(node):
    if node is None:
        return
    print(node)
    preorderSearch(node.left)
    preorderSearch(node.right)

preorderSearch(root)

# DFS - inorder search (left-node-right)
def inorderSearch(node):
    if node is None:
        return
    inorderSearch(node.left)
    print(node)
    inorderSearch(node.right)

inorderSearch(root)

# DFS - postorder search (left-right-node)
def postorderSearch(node):
    if node is None:
        return False
    postorderSearch(node.left)
    postorderSearch(node.right)
    print(node)

postorderSearch(root)


# DFS - iterative search (pre-order)
def iterativeSearch(node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)



iterativeSearch(root)

# BFS traversal (level-order search)
from collections import deque
def bfsTraversal(node):
    queue = deque()
    queue.append(node)
    while queue:
        node = queue.popleft()
        print(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

bfsTraversal(root)

# Search for a node in the tree (DFS)
def searchNode(node, target):
    if node is None:
        return False
    if node.val == target:
        return True
    return searchNode(node.left, target) or searchNode(node.right, target) # Check if the left or the right subtree contains the target
searchNode(root, 4)

# Binary Search tree Creation (left < node < right)
root2 = node(20)
A2 = node(15)
B2 = node(30)
C2 = node(10)
D2 = node(17)
root2.left = A2
root2.right = B2
A2.left = C2
A2.right = D2

# Performing an inorder traversal on BST results in a sorted tree (ascending order)
inorderSearch(root2)

# Search the BST for a target node and return true if the node is located in the tree
def searchBST(node, target):
    if node is None:
        return False
    if node.val == target:
        return True
    if node.val < target:
        return searchBST(node.right, target)
    else:
        return searchBST(node.left, target)
searchBST(root2, 17)
