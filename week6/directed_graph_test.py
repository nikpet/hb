import unittest
from directed_graph import DirectedGraph


class DirectedGraphTest(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_add_edge(self):
        self.graph.add_edge('node_a', 'node_b')
        self.graph.add_edge('node_a', 'node_c')
        self.assertEqual(self.graph.graph, {'node_a': ['node_b', 'node_c']})
        self.graph.add_edge('node_b', 'node_c')
        self.assertEqual(self.graph.graph['node_b'], ['node_c'])

    def test_get_neighbours_for(self):
        self.graph.add_edge('node_a', 'node_b')
        self.graph.add_edge('node_a', 'node_c')
        self.assertEqual(self.graph.get_neighbors_for('node_a'),
                         ['node_b', 'node_c'])

    def test_path_between(self):
        self.graph.add_edge('node_a', 'node_b')
        self.graph.add_edge('node_b', 'node_c')
        self.graph.add_edge('node_c', 'node_d')
        self.assertTrue(self.graph.path_between('node_a', 'node_d'))
        self.graph.add_edge('node_e', 'node_f')
        self.assertFalse(self.graph.path_between('node_a', 'node_f'))

if __name__ == '__main__':
    unittest.main()
