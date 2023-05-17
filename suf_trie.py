'''
Main module to create suffix trie.
'''
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    '''
    Creates a class that represents the trie node.
    '''
    def __init__(self, value = ''):
        '''
        Initializes the node.
        '''
        # Every node has a value, if it`s empty -> value=''
        self.value = value
        # Parameter to indicate if the node is a leaf:
        self.is_leaf = False

        # List of child nodes {value: Node}
        self.child = {}

    def __repr__(self) -> str:
        return str(self.value)


class SufTrie:
    '''
    Class to create a trie (suffix tree).
    '''
    def __init__(self):
        '''
        Initializes the data.
        '''
        # The root of the tree is always an empty string:
        self.root = Node('')
        self.root.is_leaf = True

    def insert_word(self, word: str) -> None:
        '''
        Inserts word into a trie.
        '''
        suffixes = SufTrie.get_suffixes(word)
        for suf in suffixes:
            node = self.root
            for i, ch in enumerate(suf):
                if ch not in node.child:
                    if node.is_leaf:
                        node.is_leaf = False
                        node.child[''] = Node()
                        node.child[''].is_leaf = False

                    node.child[ch] = Node(ch)
                    if i == len(suf) - 1:
                        node.child[ch].child[''] = Node()
                        node.child[ch].child[''].is_leaf = True

                node = node.child[ch]

    def visualise(self) -> None:
        graph = nx.Graph()
        self._build_graph(graph=graph, node=self.root)

        nx.draw(graph,
                with_labels=True,
                node_size=300,
                node_color="skyblue",
                pos=self._generate_positions(300))
        plt.title("spring")
        plt.show()

    def _build_graph(self, graph: "nx.Graph", node: "Node", parent: "Node" = None) -> None:
        graph.add_node(node)

        if parent:
            graph.add_edge(parent, node)

        if not node.is_leaf:
            for child_node in node.child.values():
                self._build_graph(graph=graph, node=child_node, parent=node)

    def _generate_positions(self, shifts: int):

        def dfs_count_pos(node: "Node", hor_shift: int = 0, vert_shift: int = 0, max_hor_shift: int = 0) -> tuple[int, dict["Node": tuple[int]]]:
            if node.is_leaf:
                return (max_hor_shift, {node: (hor_shift, vert_shift - shifts)})

            pos = {node: (max_hor_shift + shifts, vert_shift - shifts)}

            for ch_node in node.child.values():
                max_hor_shift, new_pos = dfs_count_pos(ch_node,
                                                       hor_shift=max_hor_shift + shifts,
                                                       vert_shift=vert_shift - shifts,
                                                       max_hor_shift=max_hor_shift)
                max_hor_shift += shifts
                pos.update(new_pos)

            return (max_hor_shift, pos)

        return dfs_count_pos(self.root)[1]


    @classmethod
    def draw(cls, start_node, depth = 0):
        '''
        draws a tree
        '''
        if isinstance(start_node, SufTrie):
            start_node = start_node.root

        string = ""
        tab = "│  "

        for key, node in start_node.child.items():
            line = tab * depth + key + "\n"
            string += line + SufTrie.draw(node, depth+1)

        return string

    @classmethod
    def get_suffixes(cls, word: str) -> list[str]:
        """
        returns list of suffixes of a word
        """
        return [word[begin:] for begin in range(len(word))]

if __name__ == "__main__":
    s_tree = SufTrie()
    s_tree.insert_word("lord")
    s_tree.insert_word("word")
    s_tree.insert_word("world")
    s_tree.visualise()
