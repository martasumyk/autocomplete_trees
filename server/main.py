""" Main module to start """
from flask import Flask, url_for, render_template
# import trie suf, pref

app = Flask(__name__, template_folder='../client/build', static_folder='../client/build/static')
# build trie

@app.route("/")
def main():
    return render_template("index.html")

# new autocomplete route: return json to frontend

# new suffix tree

if __name__ == "__main__":
    app.run(debug=True, port=5050)
