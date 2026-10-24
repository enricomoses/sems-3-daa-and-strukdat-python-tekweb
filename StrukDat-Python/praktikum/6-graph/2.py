from collections import deque


class Graph:
    def __init__(self):
        self.vertex = 0
        self.adj_list = {}
        self.adj_matrix = []

    def create_vertex(self, n):
        self.vertex = n
        for i in range(1, n + 1):
            self.adj_list[i] = []

    def add_edge(self, u, v):
        if u not in self.adj_list or v not in self.adj_list:
            print("Vertex tidak ditemukan")
            return

        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)

        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

    def dfs(self, start):
        visited = set()
        result = []

        def dfs_recursive(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in sorted(self.adj_list[node]):
                    dfs_recursive(neighbor)

        if start in self.adj_list:
            dfs_recursive(start)

        print("DFS:", " ".join(map(str, result)))

    def bfs(self, start):
        if start not in self.adj_list:
            return

        visited = set([start])
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in sorted(self.adj_list[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("BFS:", " ".join(map(str, result)))


graph = Graph()

while True:
    try:
        command = input().strip().split()
        if not command:
            continue

        cmd = command[0].lower()

        if cmd == "vertex":
            n = int(command[1])
            graph.create_vertex(n)

        elif cmd == "edge":
            u = int(command[1])
            v = int(command[2])
            graph.add_edge(u, v)

        elif cmd == "dfs":
            start = int(command[1])
            graph.dfs(start)

        elif cmd == "bfs":
            start = int(command[1])
            graph.bfs(start)

        elif cmd == "exit":
            break

    except EOFError:
        break


