from flask import Flask, render_template
import main

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/node")
@app.route("/node/<exemplo>")
def exemplo(exemplo: str):
    e: main.grafo = {
        ("a", 2, "b"), ("a", 2, "c"), ("a", 10, "d"), ("d", 8, "c"), ("c", 5, "h"),
        ("e", 3, "a"), ("d", 10, "e"), ("g", 30, "d"), ("g", 31, "a"), ("b", 3, "c"),
        ("g", 80, "j"), ("j", 1, "k"), ("i", 3, "k"), ("i", 5, "a"), ("j", 8, "a"),
        ("j", 6, "f"), ("j", 5, "b"), ("b", 30, "d"),
    }
    n: set[str] = set()
    n |= set(map(lambda x: x[0], e)) | set(map(lambda x: x[2], e))
    l: list[dict[str, str]] = [{'source': a, 'target': b} for a, _, b in e]
    
    return { 'nodes': [{'id': i} for i in n], 'links': l, }
