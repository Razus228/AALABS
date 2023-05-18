import networkx as nx
import random
import time
import matplotlib.pyplot as plt

def generate_random_graph(nodes):
    edge_prob = 0.1  # Smaller probability for a sparse graph

    graph = nx.fast_gnp_random_graph(nodes, edge_prob)

    for (u, v, w) in graph.edges(data=True):
        w['weight'] = random.randint(1, 100)

    return graph


def run_prim_algorithm(graph):
    start_time = time.time()
    mst = nx.minimum_spanning_tree(graph, algorithm='prim')
    end_time = time.time()
    return mst, end_time - start_time


def run_kruskal_algorithm(graph):
    start_time = time.time()
    mst = nx.minimum_spanning_tree(graph, algorithm='kruskal')
    end_time = time.time()
    return mst, end_time - start_time


def draw_graph(graph, mst, algorithm):
    pos = nx.spring_layout(graph)
    nx.draw_networkx(graph, pos, with_labels=False, node_size=100)
    nx.draw_networkx_edges(graph, pos, edgelist=mst.edges(), width=2, edge_color='r')
    plt.title(f'MST using {algorithm}')
    plt.show()


def compare_algorithms(nodes):
    prim_times = []
    kruskal_times = []

    for n in nodes:
        graph = generate_random_graph(n)

        _, prim_time = run_prim_algorithm(graph)
        prim_times.append(prim_time)

        _, kruskal_time = run_kruskal_algorithm(graph)
        kruskal_times.append(kruskal_time)

    # Plot the results
    plt.figure(figsize=(10, 6), facecolor='lightgray')
    plt.plot(nodes, prim_times, label="Prim's Algorithm", color = 'red')
    plt.plot(nodes, kruskal_times, label="Kruskal's Algorithm", color = 'blue')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Execution Time')
    plt.title('Performance of both algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()

nodes = [50, 100, 500, 1000, 2000]
compare_algorithms(nodes)

nodes = 10

graph = generate_random_graph(nodes)

mst_prim, _ = run_prim_algorithm(graph)
draw_graph(graph, mst_prim, "Prim's Algorithm")

mst_kruskal, _ = run_kruskal_algorithm(graph)
draw_graph(graph, mst_kruskal, "Kruskal's Algorithm")
