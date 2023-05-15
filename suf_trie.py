'''
Main module to create suffix trie.
'''

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
        return f"{self.value} >> {str(self.child.keys())[11:-2]}"


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
