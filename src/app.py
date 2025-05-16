from flask import Flask, render_template, request, redirect, url_for
from main import grafo, get_graph_data, add_aresta, remove_vertice

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/node")
@app.route("/node/<exemplo>")
def exemplo(exemplo=None):
    return get_graph_data()

@app.route("/add_node", methods=["POST"])
def add_node():
    origem = request.form["node_id"].strip()
    destino = request.form.get("target", "").strip()
    peso = request.form.get("value", "").strip()

    if origem and destino and peso.isdigit():
        add_aresta(origem, int(peso), destino)

    return redirect(url_for("hello_world"))

@app.route("/remove_node", methods=["POST"])
def remove_node():
    vertice = request.form.get("node_id", "").strip()
    if vertice:
        remove_vertice(vertice)
    return redirect(url_for("hello_world"))
