'''
Main module.
'''
from typing import Union
from tree import Node, Tree

class PrefixNode(Node):
    '''
    Creates a class that represents the trie node.
    '''
    def add_child(self, child: str) -> "PrefixNode":
        """add child to node

        Args:
            child (str): _description_
        """
        new_node = PrefixNode(child)
        self.children[child] = new_node

        return new_node


class PrefixTree(Tree):
    ''' Prefix Tree '''
    def __init__(self):
        super().__init__()
        self.root = PrefixNode("")

    def read_file(self, path: str):
        '''
        Read dictionary and insert words
        '''
        with open(path, 'r', encoding='utf-8') as file:
            words = file.read()

        self.build_tree(words)

    def build_tree(self, text: str):
        '''
        Build tree by reading english dict file
        '''
        for word in text.split('\n'):
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

    def autocomplete(self, prefix: str, root: Union[PrefixNode, None] = None) -> list[str]:
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
    # tree.read_file('server/words_eng.txt')

    tree.build_tree('Hello\nworld')
    tree.visualize()
