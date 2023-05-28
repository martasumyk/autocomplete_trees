# Autocomplete service and  Full text search engine

In this project we have implemented suffix and preffix trees and based on them aucomplete servise and full text search engine. Try it on our webdite - https://rabbits.pythonanywhere.com/

`Prefix tree:`

Prefix trees can be used to implement data structures like sets and associative arrays, but the most common using is when we need to search.
Each node of a prefix tree contains a single character and dictionary with children nodes and their values.


* Building:

Firstly, we built prefix tree based on the insertion of each word in the tree. The first current node of each prefix tree is always an empty string. Each node can pottentially have number of children equivalent to number of letters in alphabet (so it`s 26 for English alphabet and 33 for Ukrainian).

![image](https://github.com/martasumyk/autocomplete_trees/assets/116710765/8db8d308-a41d-4931-b8f2-0f14b6ef5e2d)

That`s how the prefix tree for the phrase "Hello world!" will look like (the orange nodes represents the end of the words).

* Compression:

When we want to compress our prefix tree, we look for nodes that have only one child and connect them into one node. With this algorithm, our tree becomes much more smaller.

* Insert word

For example, if we have word 'banana', firstly we look if in the children of current node there is letter 'b', if yes - we go deeper and do the same operations with letter 'a'. If not, we add 'b' to the list of children of our current node and then continue adding other children.
Our prefix tree support such operations: insertion of the word, compession.

`Autocomplete servise:`

Autocomplete servise shows reccomendations based on the prefix given by the user.

![image](https://github.com/martasumyk/autocomplete_trees/assets/116710765/69e989ff-d0a2-4e61-9734-c969050e1b16)

It works by recursively traversing the prefix tree and searching for the sub-words that are complete words (we have attribute is_word to check, if the nose is the end of particular word).

`Suffix tree:`

The suffix tree is another form of trie.

Each node of a suffix tree contains the value, dictionaty with children, list of indeces on which it appears in the word or phrase and attribute to store if this node is the end of a particular word.

* Building:

1. Find all the suffixes of the word or phrase. For example, if the word is 'banana' the suffixes will be 'banana', 'anana', 'nana', 'ana', 'na', 'a' and ''.

2. Insert the word or phrase by adding each of suffixes, found in point 1, to the tree.

That is how the suffix tree of the phrase "Hello world!" will look like:

![image](https://github.com/martasumyk/autocomplete_trees/assets/116710765/557243db-dd8b-451e-be0e-722a3b5c9cd4)

`Full text search engine:`

Full text search engine is used to find a pattern in the text. 

For example, I want to find "ell" in the phrase "Hello world!". 

That is how it will look like:

![image](https://github.com/martasumyk/autocomplete_trees/assets/116710765/5a7f6a5c-ca6b-4d72-99d0-cec2ebd442f1)

To perform the full text search firstly we build suffix tree for the phrase of text. Then we traverse it by the letters of the pattern that we search. If in children of current node there is no next letter, we return that the pattern does not match.

`Comparison with PostgreSQL:`

#### PostgreSQL Full Text Search:

- Uses a specialized full-text search engine built into the PostgreSQL database.
- Provides advanced features like stemming, ranking, and search operators.
- Supports various languages and allows customization of text processing and search behavior.
- Can handle large amounts of text efficiently and has better performance.
- Makes it easy to combine full-text search with other database operations.

#### Self-Written Suffix Trie-based Full Text Search:
- Based on a custom implementation of a suffix trie data structure.
- Provides a basic and simplified approach to full-text search.
- Offers a simple and lightweight solution for searching within a limited set of words or small texts.
- Does not require an external full-text search engine or database.
- Can be suitable for scenarios where you have a specific and small set of words or limited search requirements.
