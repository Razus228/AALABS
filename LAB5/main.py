import sys
import random
import time
import matplotlib.pyplot as plt

# Dijkstra's algorithm
def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distances = [sys.maxsize] * n
    distances[start] = 0

    for _ in range(n):
        min_dist = sys.maxsize
        min_index = -1
        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                min_index = i

        visited[min_index] = True
        for j in range(n):
            if (
                not visited[j]
                and graph[min_index][j] != 0
                and distances[j] > distances[min_index] + graph[min_index][j]
            ):
                distances[j] = distances[min_index] + graph[min_index][j]

    return distances


# Floyd-Warshall algorithm
def floyd_warshall(graph):
    n = len(graph)
    distances = graph.copy()

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    return distances


# Generate random sparse graph
def generate_sparse_graph(num_nodes):
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if random.random() < 0.3:  # Adjust the density as desired
                weight = random.randint(1, 10)  # Adjust the weight range as desired
                graph[i][j] = weight
                graph[j][i] = weight
    return graph


# Generate random dense graph
def generate_dense_graph(num_nodes):
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                weight = random.randint(1, 10)  # Adjust the weight range as desired
                graph[i][j] = weight
    return graph


# Empirical analysis
def empirical_analysis(num_nodes):
    # Sparse graph
    sparse_graph = generate_sparse_graph(num_nodes)

    print("Dijkstra's algorithm - Sparse Graph")
    print("Number of nodes:", num_nodes)
    start_node = 0

    start_time = time.time()
    distances_dijkstra = dijkstra(sparse_graph, start_node)
    end_time = time.time()

    print("Shortest distances from node", start_node)
    for i in range(len(distances_dijkstra)):
        print("Node", i, ": Distance =", distances_dijkstra[i])

    dijkstra_time = end_time - start_time
    print("Dijkstra's algorithm Time:", dijkstra_time, "seconds")

    # Floyd-Warshall algorithm on sparse graph
    start_time = time.time()
    distances_floyd_sparse = floyd_warshall(sparse_graph)
    end_time = time.time()

    floyd_sparse_time = end_time - start_time
    print("Floyd-Warshall algorithm Time (Sparse):", floyd_sparse_time, "seconds")

    # Dense graph
    dense_graph = generate_dense_graph(num_nodes)

    print("\nDijkstra's algorithm - Dense Graph")
    print("Number of nodes:", num_nodes)
    start_node = 0

    start_time = time.time()
    distances_dijkstra = dijkstra(dense_graph, start_node)
    end_time = time.time()

    print("Shortest distances from node", start_node)
    for i in range(len(distances_dijkstra)):
        print("Node", i, ": Distance =", distances_dijkstra[i])

    dijkstra_time = end_time - start_time
    print("Dijkstra's algorithm Time:", dijkstra_time, "seconds")

    # Floyd-Warshall algorithm on dense graph
    start_time = time.time()
    distances_floyd_dense = floyd_warshall(dense_graph)
    end_time = time.time()

    floyd_dense_time = end_time - start_time
    print("Floyd-Warshall algorithm Time (Dense):", floyd_dense_time, "seconds")

    # Plotting the differences in distances
    x = list(range(num_nodes))
    plt.figure(figsize=(10, 5))
    plt.plot(x, distances_dijkstra, label="Dijkstra's Algorithm")
    plt.plot(x, distances_floyd_sparse[0], label="Floyd-Warshall Algorithm (Sparse)")
    plt.plot(x, distances_floyd_dense[0], label="Floyd-Warshall Algorithm (Dense)")
    plt.xlabel("Node")
    plt.ylabel("Shortest Distance")
    plt.title("Comparison of Shortest Distances")
    plt.legend()
    plt.show()

    # Plotting the differences in time
    algorithms = ["Dijkstra", "Floyd-Warshall (Sparse)", "Floyd-Warshall (Dense)"]
    times = [dijkstra_time, floyd_sparse_time, floyd_dense_time]

    plt.figure(figsize=(8, 5))
    plt.bar(algorithms, times)
    plt.xlabel("Algorithm")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Algorithm Execution Times")
    plt.show()


# Test the code
num_nodes = int(input("Enter the number of nodes: "))
empirical_analysis(num_nodes)

    
