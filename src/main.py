type vertice = str
type aresta = tuple[vertice, int, vertice]
type grafo = set[aresta]

# Grafo global (modificável durante execução)
grafo: grafo = {
    ("a", 4, "b"), ("a", 8, "h"), ("b", 11, "h"), ("b", 8, "c"),
    ("c", 7, "d"), ("c", 2, "i"), ("c", 4, "f"), ("d", 9, "e"), 
    ("d", 14, "f"), ("e", 10, "f"), ("h", 1, "g"), ("i", 7, "h"), ("i", 6, "g"),
    ("g", 2, "f"),
}

# A
def kruskal(entrada: grafo) -> list[aresta]:
    ordenado = sorted(entrada, key=lambda x: x[1])
    visitados: set[vertice] = set()
    retorno: list[aresta] = []

    for conjunto in ordenado:
        a, _, b = conjunto
        if a in visitados and b in visitados:
            continue
        visitados.add(a)
        visitados.add(b)
        retorno.append(conjunto)

    return retorno

# C & B
def diff(a: grafo, b: grafo) -> list[aresta]:
    return list(a.difference(b))

# D
def verificar_arvore_geradora_minima(a: grafo) -> bool:
    return set(kruskal(a)) == a

# Suporte à adição de arestas
def add_aresta(origem: vertice, peso: int, destino: vertice) -> None:
    grafo.add((origem, peso, destino))

def remove_vertice(vertice: str) -> None:
    global grafo
    grafo = set(filter(lambda a: vertice not in (a[0], a[2]), grafo))

def get_graph_data():
    nodes = set()
    for a, _, b in grafo:
        nodes.update([a, b])
    links = [{'source': a, 'value': peso, 'target': b} for a, peso, b in grafo]
    return {
        'nodes': [{'id': n} for n in nodes],
        'links': links,
    }
