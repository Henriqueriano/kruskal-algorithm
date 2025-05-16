from flask import Flask, render_template, request, redirect, url_for, jsonify
from main import grafo, get_graph_data, add_aresta, remove_vertice, kruskal

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

@app.route("/kruskal")
def get_kruskal():
    arvore = kruskal(grafo)
    arestas_arvore = set(arvore)  # Converter para set para busca rápida
    
    nodes = set()
    for a, _, b in grafo:
        nodes.update([a, b])
    
    links = []
    for a, peso, b in grafo:
        eh_agm = (a, peso, b) in arestas_arvore or (b, peso, a) in arestas_arvore # Verifica se a aresta está na AGM
        links.append({'source': a, 'target': b, 'value': peso, 'agm': eh_agm})
    
    return jsonify({
        'nodes': [{'id': n} for n in nodes],
        'links': links
    })