def bfs(adj, n, queue, front, rear, visited):
    if front > rear:         
        return

    current = queue[front]
    print(current, end=" ")

    front += 1

    for i in range(n):
        if adj[current][i] == 1 and not visited[i]:
            visited[i] = True
            rear += 1
            queue[rear] = i   

    bfs(adj, n, queue, front, rear, visited)   


def input_matrix():
    n = int(input("Enter number of vertices: "))

    print("Enter the adjacency matrix (nxn)")
    adj = []
    for _ in range(n):
        row = list(map(int, input().split()))
        adj.append(row)

    return adj, n


def display(adj, n):
    print("\nAdjacency Matrix")
    for i in range(n):
        for j in range(n):
            print(adj[i][j], end=" ")
        print()


def main():
    adj, n = input_matrix()
    display(adj, n)

    start = int(input("\nEnter starting vertex for BFS: "))

    visited = [False] * n
    queue = [0] * n          
    front = 0
    rear = 0

    visited[start] = True
    queue[rear] = start       

    print("\nBFS Traversal: ", end="")
    bfs(adj, n, queue, front, rear, visited)
    print()


main()
