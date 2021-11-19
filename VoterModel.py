__author__ = "Ruoyun Huang"

import itertools
import random

import matplotlib.pyplot as plt
import networkx as nx


class VoterModel:
    def __init__(self, graph_node_list: [list], opinions=None):
        self.graph = nx.Graph()
        for nodes in graph_node_list:
            temp_graph = nx.Graph()
            temp_graph.add_nodes_from(nodes)
            temp_graph.add_edges_from(itertools.combinations(nodes, 2))
            self.graph = nx.compose(self.graph, temp_graph)
        if opinions:
            self.set_initial_opinion(opinions)
        else:
            self.random_opinions()

    def set_initial_opinion(self, opinions) -> None:
        for node, opinion in opinions:
            self.graph.nodes[node]["opinion"] = opinion
            self.graph.nodes[node]["opinion_history"] = [opinion]

    def random_opinions(self) -> None:
        for node in self.graph.nodes:
            opinion = random.randint(0, 1)
            self.graph.nodes[node]["opinion"] = opinion
            self.graph.nodes[node]["opinion_history"] = [opinion]

    def draw_opinion_graph(self):
        mapping = {0: "red", 1: "blue"}
        colors = [mapping[self.graph.nodes[n]['opinion']] for n in self.graph.nodes()]

        nx.draw(self.graph, with_labels=True, node_color=colors, font_weight='bold')
        plt.show()

    def iterate(self, n=1):
        for _ in range(n):
            for node in self.graph.nodes:
                neighbors = list(self.graph.neighbors(node))
                self.graph.nodes[node]["opinion"] = \
                    self.graph.nodes[random.choice(list(neighbors))]["opinion_history"][-1]
                self.graph.nodes[node]["opinion_history"].append(self.graph.nodes[node]["opinion"])
                # print(self.graph.nodes[node]["opinion_history"])


if __name__ == '__main__':
    vm = VoterModel([["stock1", "stock3", "stock5", "stock6"],
                     ["stock1", "stock2", "stock4", "stock7"]])
    vm.iterate(3)
    vm.draw_opinion_graph()
