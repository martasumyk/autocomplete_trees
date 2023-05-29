""" Main module to start """
from flask import Flask, render_template, request, jsonify
import server.prefix_trie as pt
import server.suffix_trie as st


app = Flask(__name__, template_folder='./client/build', static_folder='./client/build/static')

prefix_trie = pt.PrefixTree()
prefix_trie.build_tree('server/words.txt')

@app.route("/")
def main():
    """ Render React page """
    return render_template("index.html")

# new autocomplete route: return json to frontend
@app.route("/autocomplete", methods=['POST'])
def autocomplete():
    """ autocomplete route """
    data = request.get_json()  # Get the data sent from the frontend
    input_word = data.get("input")  # Extract the "input" value

    # print("Received input:", input_word)
    app.logger.info("Received input: %s", input_word)

    # Process the input and perform any desired operations
    response = {
        "status": "success",
        "suggestions": ", ".join(prefix_trie.autocomplete(input_word)[:7])
    }

    return jsonify(response)


# new suffix tree
@app.route("/fulltextsearch", methods=['POST'])
def full_text_search():
    """ Full text search route """
    data = request.get_json()  # Get the data sent from the frontend
    text = data.get("text")
    search = data.get("search")

    suffix_trie = st.SufTrie()
    suffix_trie.build_tree(text)

    result = suffix_trie.full_text_search_engine(search)

    return jsonify(result[0])


if __name__ == "__main__":
    app.run(debug=True, port=5050)
