
import unittest

import src.main as main


class Main(unittest.TestCase):


    def setUp(self) -> None:
        super().setUp()
        self.arestas: main.grafo = {
            ("a", 2, "b"), ("a", 2, "c"), ("a", 10, "d"), ("d", 8, "c"), ("c", 5, "h"),
            ("e", 3, "a"), ("d", 10, "e"), ("g", 30, "d"), ("g", 31, "a"), ("b", 3, "c"),
            ("g", 80, "j"), ("j", 1, "k"), ("i", 3, "k"), ("i", 5, "a"), ("j", 8, "a"),
            ("j", 6, "f"), ("j", 5, "b"), ("b", 30, "d"),
        }


    def test_kruskal(self):

        esperado: list[main.aresta] = [('j', 1, 'k'), ('a', 2, 'b'), ('a', 2, 'c'), ('e', 3, 'a'),
                                       ('i', 3, 'k'), ('c', 5, 'h'), ('j', 6, 'f'), ('d', 8, 'c'), ('g', 30, 'd')]

        resultado = main.kruskal(self.arestas)

        self.assertSetEqual(set(resultado), set(esperado))

    def test_diff(self):
        resultado = main.diff(self.arestas, set(main.kruskal(self.arestas)))
        esperado = [('g', 31, 'a'), ('b', 30, 'd'), ('i', 5, 'a'), ('a', 10, 'd'), ('j', 8, 'a'),
                    ('j', 5, 'b'), ('b', 3, 'c'), ('g', 80, 'j'), ('d', 10, 'e')]
        self.assertSetEqual(set(resultado), set(esperado))

    def test_verificar(self):
        grafo: main.grafo = {('j', 1, 'k'), ('a', 2, 'b'), ('a', 2, 'c'), ('e', 3, 'a'),
                             ('i', 3, 'k'), ('c', 5, 'h'), ('j', 6, 'f'), ('d', 8, 'c'), ('g', 30, 'd')}
        resultado = main.verificar_arvore_geradora_minima(grafo)
        self.assertTrue(resultado)




if __name__ == '__main__':
    unittest.main()
