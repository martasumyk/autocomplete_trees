""" Main module to start """
from flask import Flask, url_for, render_template
import server.pref_trie as pt
import server.suf_trie as st
import json

app = Flask(__name__, template_folder='./client/build', static_folder='./client/build/static')
# build pref_trie
prefix_trie = pt.PrefixTree()
prefix_trie.build_tree('words_eng.txt')

@app.route("/")
def main():
    return render_template("index.html")

# new autocomplete route: return json to frontend
@app.route("/pref", methods=['POST'])
def prefix():
    pass

# new suffix tree
@app.route("/suf", methods=['POST'])
def sufix():
    pass

if __name__ == "__main__":
    app.run(debug=True, port=5050)
