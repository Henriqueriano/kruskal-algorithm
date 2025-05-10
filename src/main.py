


type vertice = str
type aresta = tuple[vertice, int, vertice]
type grafo = set[aresta] # pressupõe que não estamos trabalhando com um grafo desconexo

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

# E
# usar imaginação.


