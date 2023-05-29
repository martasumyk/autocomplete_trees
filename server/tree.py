''' Module tree '''
from typing import Union

import networkx as nx
import matplotlib.pyplot as plt

class Node:
    '''
    Creates a class that represents the trie node.
    '''
    def __init__(self, value: str = "", is_word = False):
        '''
        Initializes the node.
        '''
        # Every node has a value, if it`s empty -> value=''
        self.value = value
        self.is_word = is_word

        # List of child nodes:
        self.children: dict[str, "Node"] = {}

    def __str__(self) -> str:
        return f"Node({self.value}). Is word {self.is_word}. Children: {list(self.children.keys())}"


class Tree:
    '''
    General class to create prefix/suffix tree.
    '''
    def __init__(self):
        '''
        Initializes the tree. The root is always a node with an empty string.
        '''
        self.root = Node("")


    def compress_tree(self, root: Union[Node, None] = None):
        ''' ArithmeticError '''
        node = root or self.root

        if len(node.children) == 1 and not node.is_word:
            child = node.children[list(node.children.keys())[0]]
            node.value += child.value
            node.children = child.children
            node.is_word = child.is_word

            self.compress_tree(child)
        else:
            for child in node.children.values():
                self.compress_tree(child)

    def build_tree(self, text: str):
        ''' build tree '''
        raise NotImplementedError


    def visualize(self) -> None:
        """
        creates NetworkX graph, positions it's nodes and colorises them
        """
        graph = nx.Graph()
        self._build_nx_graph(graph=graph, node=self.root)

        nx.draw(graph,
                with_labels=True,
                node_size=300,
                node_color=self._generate_colors(graph),
                pos=self._generate_positions(300))
        plt.title("spring")
        plt.show()

    def _build_nx_graph(self, graph: "nx.Graph", node: "Node", parent: "Node" = None) -> None:
        """
        recursively fills graph with nodes of the Tree
        """
        graph.add_node(node)

        if parent:
            graph.add_edge(parent, node)

        for child_node in node.children.values():
            self._build_nx_graph(graph=graph, node=child_node, parent=node)

    def _generate_colors(self, graph: "nx.Graph", main_c='lightblue', end_c='lightsalmon'):
        """
        parces graph and node's parameter is_word == True, sets it's color to end_c, else to main_c
        """
        color_map = []
        for vert in graph:
            if vert.is_word:
                color_map.append(end_c)
            else:
                color_map.append(main_c)
        return color_map

    def _generate_positions(self, shifts: int):
        """
        generates a dictionary of postions

        shifts: distances between nodes
        """
        def dfs_count_pos(node: "Node", vert_shift: int = 0, max_hor_shift: int = 0)\
             -> tuple[int, dict["Node": tuple[int]]]:
            """
            recursive dfs that sets positions to every node
            saves max_hor_shift to avoid intersection of nodes
            """
            if node is None:
                return (max_hor_shift, {})

            pos = {node: (max_hor_shift, vert_shift - shifts)}

            for ch_node in node.children.values():
                max_hor_shift, new_pos = dfs_count_pos(ch_node,
                                                       vert_shift=vert_shift - shifts,
                                                       max_hor_shift=max_hor_shift)
                if len(node.children) > 1:
                    max_hor_shift += shifts
                pos.update(new_pos)

            if len(node.children) > 1:
                max_hor_shift -= shifts

            return (max_hor_shift, pos)

        return dfs_count_pos(self.root)[1]
