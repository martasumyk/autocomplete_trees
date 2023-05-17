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
                    # first iteration
                    if node.is_leaf:
                        node.is_leaf = False
                        node.child[''] = Node()
                        node.child[''].is_leaf = True

                    node.child[ch] = Node(ch)
                    if i == len(suf) - 1:
                        node.child[ch].child[''] = Node()
                        node.child[ch].child[''].is_leaf = True

                node = node.child[ch]
            node.child[''] = Node()
            node.child[''].is_leaf = True

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
        """
        generates a dictionary of postions

        shifts: distances between nodes
        """
        def dfs_count_pos(node: "Node", vert_shift: int = 0, max_hor_shift: int = 0)\
             -> tuple[int, dict["Node": tuple[int]]]:
            """
            recursive dfs that sets positions to evry node
            saves max_hor_shift to avoid intersection of nodes
            """
            if node is None:
                return (max_hor_shift, {})

            pos = {node: (max_hor_shift, vert_shift - shifts)}

            for ch_node in node.child.values():
                max_hor_shift, new_pos = dfs_count_pos(ch_node,
                                                       vert_shift=vert_shift - shifts,
                                                       max_hor_shift=max_hor_shift)
                if len(node.child) > 1:
                    max_hor_shift += shifts
                pos.update(new_pos)

            if len(node.child) > 1:
                    max_hor_shift -= shifts

            return (max_hor_shift, pos)

        return dfs_count_pos(self.root)[1]

    @classmethod
    def get_suffixes(cls, word: str) -> list[str]:
        """
        returns list of suffixes of a word
        """
        return [word[begin:] for begin in range(len(word))]

if __name__ == "__main__":
    s_tree = SufTrie()
    s_tree.insert_word("banana")
    s_tree.visualise()
