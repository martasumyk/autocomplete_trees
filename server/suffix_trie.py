'''
Main module to create suffix trie.
'''
from server.tree import Node, Tree

class SuffixNode(Node):
    '''
    Creates a class that represents the trie node.
    '''
    def __init__(self, value: str = "", idx = None, is_word=False):
        super().__init__(value, is_word)
        self.idx = [idx]

    def __str__(self) -> str:
        return f"value: {self.value}\nindexes:{self.idx}"
        # return str(self.value)
        # return str(self.idx)


class SufTrie(Tree):
    '''
    Class to create a trie (suffix tree).
    '''
    def __init__(self):
        '''
        Initializes the data.
        '''
        # The root of the tree is always an empty string:
        super().__init__()
        self.root = SuffixNode('')

    def build_tree(self, text: str) -> None:
        '''
        Inserts text into a trie.
        '''
        suffixes = SufTrie.get_suffixes(text)
        for index, suf in enumerate(suffixes):
            node = self.root
            for char in suf:
                if char not in node.children:
                    node.children[char] = SuffixNode(char, idx=index)
                else:
                    node.children[char].idx.append(index)

                node = node.children[char]
            node.is_word = True

    @classmethod
    def get_suffixes(cls, word: str) -> list[str]:
        """
        returns list of suffixes of a word
        """
        return [word[begin:] for begin in range(len(word))]

    def full_text_search_engine(self, pattern: str):
        '''
        Searches the pattern in the text traversing it`s suffix tree.
        '''
        current_node = self.root
        start_indeces = []
        for letter in pattern:
            if letter not in current_node.children:
                return [[]]

            current_node = current_node.children[letter]

        # Counting start and end index, where the text matches pattern:
        start_indeces = current_node.idx
        end_indeces = [i + len(pattern) for i in start_indeces]
        return start_indeces, end_indeces

if __name__ == "__main__":
    s_tree = SufTrie()
    sentence = "banana"

    s_tree.build_tree(sentence)
    s_tree.visualize()
