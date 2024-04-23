from collections import deque#Ленивый Поиск в Ширину (Breadth-FirstSearch)-Реализовать ленивый алгоритм поиска в ширину для графа или дерева.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def lazy_bfs(self, start, condition_func):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if condition_func(node):
                return node

            visited.add(node)
            neighbors = self.graph.get(node, [])
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)

        return None

# Пример использования
def is_goal_node(node):
    return node == 'G'

g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'G')

start_node = 'A'
goal_node = g.lazy_bfs(start_node, is_goal_node)

if goal_node:
    print(f"Ближайший узел, удовлетворяющий условию, найден: {goal_node}")
else:
    print("Ни один узел не удовлетворяет условию")

