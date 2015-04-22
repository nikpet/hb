class DirectedGraph():
    def __init__(self):
        self.graph = {}

    def add_edge(self, node_a, node_b):
        if node_a in self.graph:
            self.graph[node_a].append(node_b)
        else:
            self.graph[node_a] = [node_b]

    def get_neighbors_for(self, node):
        return self.graph[node]

    def path_between(self, node_a, node_b):
        queue = self.graph[node_a]
        visited = {node_a}
        found = False

        while len(queue) > 0:
            current = queue.pop(0)
            visited.add(current)
            if current == node_b:
                found = True
                break
            for item in self.graph[current]:
                if item not in visited:
                    visited.add(item)
                    queue.append(item)
        return found
