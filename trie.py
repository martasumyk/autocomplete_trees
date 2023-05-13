'''
Main module to create prefix trie.
'''

class Node:
    '''
    Creates a class that represents the trie node.
    '''
    def __init__(self, value):
        '''
        Initializes the node.
        '''
        # Every node has a value, if it`s empty -> value=''
        self.value = value
        # Parameter to indicate if the node is a leaf:
        self.is_leaf = False

        # List of child nodes:
        self.child = []


class Trie:
    '''
    Class to create a trie (prefix tree).
    '''
    def __init__(self):
        '''
        Initializes the data.
        '''
        # The root of the tree is always an empty string:
        self.root = Node('')

    def insert_word(self):
        '''
        Inserts word into a trie.
        '''
        pass

    def delete_word(self):
        '''
        Deletes the word from the trie.
        '''
        pass

    def find_words(self, prefix):
        '''
        Finds all the words that starts with prefix.
        '''
        pass
