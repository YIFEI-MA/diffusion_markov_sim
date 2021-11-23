import itertools
import random

import matplotlib.pyplot as plt
import networkx as nx


def initialize_graph(graph_node_list: list) -> nx.Graph:
    g = nx.Graph()
    for nodes in graph_node_list:
        temp_graph = nx.Graph()
        temp_graph.add_nodes_from(nodes)
        temp_graph.add_edges_from(itertools.combinations(nodes, 2))
        g = nx.compose(g, temp_graph)
    return g


def random_opinions(graph: nx.Graph) -> None:
    for node in graph.nodes:
        opinion = random.randint(0, 1)
        graph.nodes[node]["opinion"] = opinion
        graph.nodes[node]["opinion_history"] = [opinion]


def set_initial_opinion(graph: nx.Graph, opinions: [tuple]) -> None:
    for node, opinion in opinions:
        graph.nodes[node]["opinion"] = opinion
        graph.nodes[node]["opinion_history"] = [opinion]


def draw_opinion_graph(graph: nx.Graph):
    mapping = {0: "red", 1: "blue"}
    colors = [mapping[graph.nodes[n]['opinion']] for n in graph.nodes()]

    nx.draw(graph, with_labels=True, node_color=colors, font_weight='bold')
    plt.show()
