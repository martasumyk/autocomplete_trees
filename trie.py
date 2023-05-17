'''
Main module.
'''
from typing import Union
# import networkx as nx
# import matplotlib.pyplot as plt

class Node:
    '''
    Creates a class that represents the trie node.
    '''
    def __init__(self, value: str, parent: Union["Node", None], is_word = False):
        '''
        Initializes the node.
        '''
        # Every node has a value, if it`s empty -> value=''
        self.value = value

        # List of child nodes:
        self.children: dict[str, "Node"] = {}
        self.parent = parent
        self.is_word = is_word

    def add_child(self, child: str) -> "Node":
        """add child to node

        Args:
            child (str): _description_
        """
        new_node = Node(child, self)
        self.children[child] = new_node

        return new_node

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
        self.root = Node("", None)

        # Creating a graph to visualize a tree:
        # self.graph = nx.Graph()


    # def draw_graph(self):
    #     '''
    #     Visualizes the graph.
    #     '''
    #     plt.figure(figsize=(10, 6))

    #     pos = nx.arf_layout(graph)
    #     nx.draw(graph, pos, node_color='lightblue',
    #             with_labels=True,
    #             node_size=500,
    #             arrowsize=20,
    #             arrows=True)
    #     labels = nx.get_edge_attributes(graph, 'weight')
    #     nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    #     plt.show()

    # def create_graph(self, tree, index = 0):
    #     '''
    #     Creates a graph from tree.
    #     '''
    #     if tree.parent:
    #         self.graph.add_node(tree.value + str(index))
    #         self.graph.add_edge(tree.value + str(index), tree.parent.value + str(index - 1))

    #     for child in tree.children.values():
    #         self.create_graph(child, index + 1)


class PrefixTree(Tree):
    ''' Prefix Tree '''
    def build_tree(self, path: str):
        '''
        Build tree by reading english dict file
        '''
        with open(path, 'r', encoding='utf-8') as file:
            words = file.read().split('\n')

        for word in words:
            self.insert_word(word.strip())

        self.compress_tree()

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

    def insert_word(self, word: str):
        '''
        Inserts word into a trie.
        '''
        node = self.root

        for letter in word:
            if letter in node.children:
                node = node.children[letter]
                continue

            node = node.add_child(letter)

        node.is_word = True

    def autocomplete(self, prefix: str, root: Union[Node, None] = None) -> list[str]:
        '''
        Finds all the words that starts with prefix.
        '''
        node = root or self.root
        words: list[str] = []

        # if we first time in this function
        if node == self.root:
            # try to find a sub-word in a tree
            for letter in prefix:
                if letter not in node.children:
                    # Unknown word
                    return []

                node = node.children[letter]

            # if sub-word is a complete word
            if node.is_word:
                words.append(prefix)

        # go to every child and recursively call this function
        for child in node.children:
            node_child = node.children[child]
            value = node_child.value

            if node_child.is_word:
                words.append(prefix + value)

            words += [(prefix + suffix) for suffix in self.autocomplete(value, node_child)]

        return words

if __name__ == "__main__":
    tree = PrefixTree()
    tree.build_tree('words.txt')

    # TODO: fix bananaq and bananaqu
    print( tree.autocomplete('banana') )
    print( tree.autocomplete('bananaq') )
    print( tree.autocomplete('bananaqu') )
