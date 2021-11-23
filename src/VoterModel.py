__author__ = "Ruoyun Huang"

import itertools
import random
from math import exp

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class VoterModel:
    def __init__(self, graph_node_list: [list], price, opinions=None):
        """
        Initialize voter model object
        :param graph_node_list: [list]
        :param price: list that contains price of all the nodes
        :param opinions: list that contains opinion of all the nodes
        """
        self.graph = nx.Graph()
        for nodes in graph_node_list:
            temp_graph = nx.Graph()
            temp_graph.add_nodes_from(nodes)
            temp_graph.add_edges_from(itertools.combinations(nodes, 2))
            self.graph = nx.compose(self.graph, temp_graph)

        if opinions:
            self.set_initial_opinion(opinions)
        else:
            # if opinion is None, we randomly set it
            self.random_opinions()
        self.set_initial_price(price)

    def set_initial_price(self, price) -> None:
        """
        Initialize price of beginning(t0)
        :param price: a list that contains price of all the nodes
        """
        for node in self.graph.nodes:
            if node in price:
                self.graph.nodes[node]["price"] = [price[node]]
            else:
                self.graph.nodes[node]["price"] = [None]

    def set_initial_opinion(self, opinions) -> None:
        """
        Set Initial opinion of t0
        :param opinions: a list that contains opinion of all the nodes
        :return: None
        """
        for node, opinion in opinions:
            self.graph.nodes[node]["opinion"] = opinion
            self.graph.nodes[node]["opinion_history"] = [opinion]

    def random_opinions(self) -> None:
        """
        randomly set initial opinions
        :return: None
        """
        for node in self.graph.nodes:
            opinion = random.randint(0, 1)
            self.graph.nodes[node]["opinion"] = opinion
            self.graph.nodes[node]["opinion_history"] = [opinion]

    def draw_opinion_graph(self) -> None:
        """
        Draw the figure of the graph
        :return: None
        """
        mapping = {0: "red", 1: "blue"}
        colors = [mapping[self.graph.nodes[n]['opinion']] for n in self.graph.nodes()]
        nx.draw(self.graph, with_labels=True, node_color=colors, font_weight='bold')
        plt.show()

    def iterate(self, n, individual_returns: dict, market_returns: dict, betas: dict, sigmas: dict) -> None:
        """
        Iterate for n times, for both of voter model simulation and brownian motion
        :param n: int
        :param individual_returns: a dictionary of individual return of each stock
        :param market_returns: a dictionary of of market returns of each stock
        :param betas: a dictionary of of beta of each stock
        :param sigmas: a dictionary of of sigma of each stock
        :return: None
        """
        for i in range(1, n+1):
            for node in self.graph.nodes:
                neighbors = list(self.graph.neighbors(node))
                self.graph.nodes[node]["opinion"] = \
                    self.graph.nodes[random.choice(neighbors)]["opinion_history"][-1]
                if self.graph.nodes[node]["opinion"]:
                    market_r = abs(market_returns[node])
                else:
                    market_r = -abs(market_returns[node])
                current_price = self.graph.nodes[node]["price"][0] * exp(
                    individual_returns[node] + market_r * betas[node]) - sigmas[node] * \
                    np.random.normal(0, i, 1)[0]
                self.graph.nodes[node]["price"].append(current_price)
            for node in self.graph.nodes:
                self.graph.nodes[node]["opinion_history"].append(self.graph.nodes[node]["opinion"])

    def show_price_history(self) -> None:
        """
        Print out stock price over time
        :return: None
        """
        for node in self.graph.nodes:
            prices = self.graph.nodes[node]["price"]
            print("\n{:10s}".format(node), end='')
            for p in prices:
                print("\t{:10.4f}".format(p), end='')


if __name__ == '__main__':
    vm = VoterModel([["stock1", "stock3", "stock5", "stock6", "h"],
                     ["stock1", "stock2", "stock4", "stock7"],
                     ["h", "a", 'b']], {}, None)
    vm.draw_opinion_graph()
