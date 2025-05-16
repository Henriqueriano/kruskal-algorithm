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
        ("a", 4, "b"), ("a", 8, "h"), ("b", 11, "h"), ("b", 8, "c"),
        ("c", 7, "d"), ("c", 2, "i"), ("c", 4, "f"), ("d", 9, "e"), 
        ("d", 14, "f"), ("e", 10, "f"), ("h", 1, "g"), ("i", 7, "h"), ("i", 6, "g"),
        ("g", 2, "f"),
    }
    n: set[str] = set()
    n |= set(map(lambda x: x[0], e)) | set(map(lambda x: x[2], e))
    l: list[dict[str, int, str]] = [{'source': a, 'value': value, 'target': b} for a, value, b in e]
    
    return { 'nodes': [{'id': i} for i in n], 'links': l, }
