class Graph:
    def __init__(self):
        self.vertex = 0
        self.adj_list = {}
        self.adj_matrix = []

    def create_vertex(self, n):
        self.vertex = n
        for i in range(1, n + 1):
            self.adj_list[i] = []

        self.adj_matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(0)
            self.adj_matrix.append(row)

    def add_edge(self, u, v):
        if u not in self.adj_list or v not in self.adj_list:
            print("Vertex tidak ditemukan")
            return

        if v not in self.adj_list[u]:
            self.adj_list[u].append(v)

        if u not in self.adj_list[v]:
            self.adj_list[v].append(u)

        self.adj_matrix[u - 1][v - 1] = 1
        self.adj_matrix[v - 1][u - 1] = 1

    def show_adj_list(self):
        print("Adjacency List:")
        for i in range(1, self.vertex + 1):
            neighbors = sorted(self.adj_list[i])
            print(f"{i}: {', '.join(map(str, neighbors))}")

    def show_adj_matrix(self):
        print("Adjacency Matrix:")
        header = "   " + " ".join(str(i) for i in range(1, self.vertex + 1))
        print(header)
        for i in range(1, self.vertex + 1):
            row_str = " ".join(str(val) for val in self.adj_matrix[i - 1])
            print(f"{i}: {row_str}")


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

        elif cmd == "show":
            graph.show_adj_list()
            print()
            graph.show_adj_matrix()

        elif cmd == "exit":
            break

    except EOFError:
        break

