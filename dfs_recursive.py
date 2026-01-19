

def dfs(adj, n, current, visited):
    visited[current] = True
    print(current, end=" ")

    for i in range(n):
        if adj[current][i] == 1 and not visited[i]:
            dfs(adj, n, i, visited)


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

    start = int(input("\nEnter starting vertex for DFS: "))

    visited = [False] * n
    print("\nDFS Traversal: ", end="")
    dfs(adj, n, start, visited)
    print()


if __name__ == "__main__":
    main()
