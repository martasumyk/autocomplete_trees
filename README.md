# Autocomplete service and  Full text search engine

In this project we have implemented suffix and preffix trees and based on them aucomplete servise and full text search engine.

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
