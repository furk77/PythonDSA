# Array of Edges (Edge List) (Directed) [Start, End]
numberofNodes = 8
A = [[0, 1], [1, 2], [0, 3], [3, 4], [3, 6], [3, 7], [4, 2], [4, 5], [5, 2]]

print(A)

# Converting Edge List to Adjacency List
adjMatrix = []
for i in range(numberofNodes): # Traverse through all the vertices and append a list for every one of them
  adjMatrix.append([0] * numberofNodes)

for r, c in A:
  adjMatrix[r][c] = 1 # Traverse through the edge list and mark the edge locations with 1 in the adj matrix

  # Uncomment the following line if the graph is undirected
  # adjMatrix[c][r] = 1

print(adjMatrix)

# Converting Edge List to Adjacency List
adjMatrix = []
for i in range(numberofNodes): # Traverse through all the vertices and append a list for every one of them
  adjMatrix.append([0] * numberofNodes)

for r, c in A:
  adjMatrix[r][c] = 1 # Traverse through the edge list and mark the edge locations with 1 in the adj matrix

  # Uncomment the following line if the graph is undirected
  # adjMatrix[c][r] = 1

print(adjMatrix)

# Converting Edge List to Adjacency List
from collections import defaultdict

adjList = defaultdict(list)

for u, v in A:
  adjList[u].append(v)
  # Uncomment the following line if the graph is undirected
  # D[v].append(u)

print(adjList)
print(adjList[0])

# DFS with Recursion - O(V + E) where V is the number of nodes and E is the number of edges

def dfs_recursive(node):
  print(node)
  for nei_node in adjList[node]:
    if nei_node not in seen:
      seen.add(nei_node)
      dfs_recursive(nei_node)

source = 0
seen = set()
seen.add(source)
dfs_recursive(source)

# Iterative DFS with Stack - O(V + E)

source = 0

seen = set()
seen.add(source)
stack = [source]

while stack:
  node = stack.pop()
  print(node)
  for nei_node in D[node]:
    if nei_node not in seen:
      seen.add(nei_node)
      stack.append(nei_node)

# Breadth First Search for Graphs (Uses a set to keep track of visited nodes/vertices)
from collections import deque
def bfsGraph(graph, start):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

bfsGraph(adjList, 0)

# Graph representation with a node class
class node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
    def __str__(self):
        return str(self.val)
    def display(self):
        connections = [node.val for node in self.neighbors]
        print(f"{self.val} is connected to {connections}")

A = node('A')
B = node('B')
C = node('C')
D = node('D')
E = node('E')
F = node('F')
G = node('G')

A.neighbors = [B, C]
B.neighbors = [A, D]
C.neighbors = [A, E, F]
D.neighbors = [B, E]
E.neighbors = [C, D, F, G]

A.display()
E.display()
print(B)
