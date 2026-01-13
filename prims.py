"""v=int(input("Enter number of vertices"))
e=int(input("Enter number of edges"))
visited=[0]*v
inf=999

adj=[[inf for j in range(v)] for i in range(v)]

for i in range (0,v):
    for j in range (0,v):
        if(i==j):
            adj[i][j]=0
        else:
            adj[i][j]=inf;
            
for i in range (0,e):
    print("Enter the city nodes")
    u1=int(input())
    u2=int(input())
    
    w=int(input("Enter weight"))
    
    adj[u2][u1]=w;
    adj[u1][u2]=w;
    
visited[0]=1
totalcost=0
edges=0
while(edges< v-1):
    min=inf
    a=-1
    b=-1
    
    for i in range (0,v):
        if(visited[i]):
            for j in range (0,v):
                if(visited[j]==0 and adj[i][j]<min):
                    min=adj[i][j]
                    a=i
                    b=j
                    
    if(a!= -1 and b!=-1):
        print("route ", edges ,"selected : ", a ,"-", b , "cost : ", adj[a][b])
        print()
        visited[b]=1
        totalcost += adj[a][b]
        edges +=1
       
       
print("Total cost of the minimum spanning tree: ", totalcost)
print()"""


v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

visited = [0] * v
inf = 999

# Create adjacency matrix
adj = [[inf for j in range(v)] for i in range(v)]

# Initialize diagonal to 0
for i in range(0, v):
    for j in range(0, v):
        if i == j:
            adj[i][j] = 0
        else:
            adj[i][j] = inf

# Input edges
for i in range(0, e):
    print("Enter the city nodes")
    u1 = int(input())
    u2 = int(input())
    w = int(input("Enter weight: "))

    adj[u2][u1] = w
    adj[u1][u2] = w

# Print adjacency matrix
print("\nAdjacency Matrix:")
for i in range(v):
    for j in range(v):
        if adj[i][j] == inf:
            print("INF", end="\t")
        else:
            print(adj[i][j], end="\t")
    print()

# Prim's Algorithm
visited[0] = 1
totalcost = 0
edges = 0

print("\nSelected edges in MST:")

while edges < v - 1:
    min = inf
    a = -1
    b = -1

    for i in range(0, v):
        if visited[i]:
            for j in range(0, v):
                if visited[j] == 0 and adj[i][j] < min:
                    min = adj[i][j]
                    a = i
                    b = j

    if a != -1 and b != -1:
        print("route", edges + 1, "selected :", a, "-", b, "cost :", adj[a][b])
        visited[b] = 1
        totalcost += adj[a][b]
        edges += 1

print("\nTotal cost of the minimum spanning tree:", totalcost)

                    


