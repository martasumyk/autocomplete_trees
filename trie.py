'''
Main module to create prefix trie.
'''
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    '''
    Creates a class that represents the trie node.
    '''
    def __init__(self, value: str, parent: "Node", is_word = False):
        '''
        Initializes the node.
        '''
        # Every node has a value, if it`s empty -> value=''
        self.value = value
        # Parameter to indicate if the node is a leaf:
        self.is_leaf = False

        # List of child nodes:
        self.children = {}
        self.parent = parent
        self.is_word = is_word

    def add_child(self, child: str) -> None:
        """add child to node

        Args:
            child (str): _description_
        """
        new_node = Node(child, self)
        self.children[child] = new_node

        return new_node


class Trie:
    '''
    Class to create a trie (prefix tree).
    '''
    def __init__(self):
        '''
        Initializes the data.
        '''
        # The root of the tree is always an empty string:
        self.root = Node("", None)

    def build_tree(self, path):
        '''
        Build tree by reading english dict file
        '''
        with open(path, 'r', encoding='utf-8') as file:
            words = file.read().split('\n')

        for word in words:
            self.insert_word(word.strip())

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

    def delete_word(self):
        '''
        Deletes the word from the trie.
        '''
        raise NotImplementedError()


    def find_words(self, prefix):
        '''
        Finds all the words that starts with prefix.
        '''
        raise NotImplementedError()

    def autocomplete(self, prefix: str, root = None):
        node = root or self.root
        words = []

        if node == self.root:
            for letter in prefix:
                node = node.children[letter]

        for child in node.children:
            node_child = node.children[child]

            if node_child.is_word:
                words.append(prefix + node_child.value)

            words += [prefix + i for i in self.autocomplete(node_child.value, node_child)]

        return words


trie = Trie()
trie.build_tree('words_eng.txt')
print(trie.autocomplete('banana'))

# def draw_graph(graph):
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


# graph = nx.Graph()
# def create_graph(tree, index = 0):
#     if tree.parent:
#         graph.add_node(tree.value + str(index))
#         graph.add_edge(tree.value + str(index), tree.parent.value + str(index - 1))

#     for child in tree.children.values():
#         create_graph(child, index + 1)

# create_graph(trie.root)
# draw_graph(graph)
# print(trie.root.children)