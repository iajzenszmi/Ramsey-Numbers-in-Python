import itertools

def is_ramsey(graph, m, k):
    n = len(graph)
    for nodes in itertools.combinations(range(n), min(m, k)):
        all_red = all(graph[u][v] for u, v in itertools.combinations(nodes, 2))
        all_blue = not any(graph[u][v] for u, v in itertools.combinations(nodes, 2))
        if all_red or all_blue:
            return True
    return False

def ramsey_number(m, k):
    n = max(m, k)
    while True:
        # Generate all possible graphs of size n
        for graph in itertools.product([False, True], repeat=n*(n-1)//2):
            # Convert graph to adjacency matrix form
            adj_matrix = [[False] * n for _ in range(n)]
            edge_index = 0
            for i in range(n):
                for j in range(i + 1, n):
                    adj_matrix[i][j] = adj_matrix[j][i] = graph[edge_index]
                    edge_index += 1

            if is_ramsey(adj_matrix, m, k):
                return n
        n += 1

# Example of calculating a small Ramsey number
print(ramsey_number(3, 3))
import itertools

def is_ramsey(graph, m, k):
    n = len(graph)
    for nodes in itertools.combinations(range(n), min(m, k)):
        all_red = all(graph[u][v] for u, v in itertools.combinations(nodes, 2))
        all_blue = not any(graph[u][v] for u, v in itertools.combinations(nodes, 2))
        if all_red or all_blue:
            return True
    return False

def ramsey_number(m, k):
    n = max(m, k)
    while True:
        # Generate all possible graphs of size n
        for graph in itertools.product([False, True], repeat=n*(n-1)//2):
            # Convert graph to adjacency matrix form
            adj_matrix = [[False] * n for _ in range(n)]
            edge_index = 0
            for i in range(n):
                for j in range(i + 1, n):
                    adj_matrix[i][j] = adj_matrix[j][i] = graph[edge_index]
                    edge_index += 1

            if is_ramsey(adj_matrix, m, k):
                return n
        n += 1

# Example of calculating a small Ramsey number
print(ramsey_number(50, 50))
