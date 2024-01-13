class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dic = {}
        for start, end in self.edges:
            if start in self.dic:
                self.dic[start].append(end)
            else:
                self.dic[start] = [end]
        print ("Graph dict:",self.dic)


    def get_path(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.dic:
            return []
        
        paths = []

        for node in self.dic[start]:
            if node not in path:
                new_path = self.get_path(node, end, path)
                for p in new_path:
                    paths.append(p)

        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.dic:
            return None

        shortest_path = None
        for node in self.dic[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path




if __name__ == "__main__":
    routes = [
        ("Karachi","Lahore"),
        ("Lahore", "Gujjrat"),
        ("Lahore", "Dubai"),
        ("Faisalabad","Rawalpindi"),
        ("Toronto","Dubai"),
        ("Dubai","Toronto"),
        ("Lahore", "Toronto"),
        ("Karachi", "Toronto"),
        ("Karachi", "Dubai")
    ]

    graph = Graph(routes)

    start = 'Lahore'
    end = 'Toronto'

    print ("The Path between {start} and {end} is", graph.get_shortest_path(start, end) )