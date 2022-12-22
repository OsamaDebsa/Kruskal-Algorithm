def kruskal(NumVertices, edges):
  edges.sort()

  MSet = []
  for v in range(NumVertices):
    MSet.append(v)

  rank = [0] * NumVertices  # Add this line to define rank

  MST = []

  def find(parent, i):
    if parent[i] == i:
      return i
    return find(parent, parent[i])

  def union(parent, rank, x, y):
    X_Root = find(parent, x)
    Y_Root = find(parent, y)

    if rank[X_Root] < rank[Y_Root]:
      parent[X_Root] = Y_Root

    elif rank[X_Root] > rank[Y_Root]:
      parent[Y_Root] = X_Root

    else:
      parent[Y_Root] = X_Root
      rank[X_Root] += 1

  for w, u, v in edges:
    if find(MSet, u) != find(MSet, v):
      MST.append((u, v, w))
      union(MSet, rank, u, v)
  return MST

NumVertices = int(input("Enter The Number Of Vertices : "))
NumEdges = int(input("Enter The Number Of Edges : "))

edges = []
for i in range(NumEdges):
  u, v, w = map(int, input("Enter edge (u v w): ").split())
  edges.append((w, u, v))

MST = kruskal(NumVertices, edges)
print("Minimum Spanning Tree : ", MST)

cost = 0
for u, v, w in MST:
  cost += w
print("Cost of MST:", cost)

''' 
Test The Code :
  Enter The Number Of Vertices : 4
  Enter The Number Of Edges : 5
  Enter edge (u v w): 0 1 5
  Enter edge (u v w): 0 2 3
  Enter edge (u v w): 1 2 4
  Enter edge (u v w): 1 3 2
  Enter edge (u v w): 2 3 1

Minimum Spanning Tree :  [(0, 2, 3), (2, 3, 1), (1, 3, 2)]
Cost of MST: 6
'''