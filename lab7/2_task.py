class Graph:
    id_name = {}
    graph = {}
    way = []
    
    def loadfromfile(self, file):
        with open(file) as f:
            f.readline()
            names = f.readline().split()
            for item in names:
                item = item.replace(',', '')
                item = item.split(':')
                id, name = item[0], item[1]
                self.graph.setdefault(name, {})
                self.id_name[int(id)] = name
            index = 1
            for line in f:
                for way in line.split():
                    key = self.id_name[index]
                    if int(way) > 0:
                        self.graph[key].setdefault(self.id_name[line.split().index(way) + 1], int(way))
                index += 1
        return self.graph

    costs = {}
    checked_node = []

    def find_costs(self, start_point):
        neighbors = self.graph[start_point]
        self.costs[start_point] = 0
        for key in neighbors.keys():
            if key not in self.checked_node:
                self.costs[key] = neighbors[key]
            for value in self.id_name.values():
                if value not in self.costs:
                    self.costs[value] = float('inf')
        return self.costs

    def find_lowest_cost_node(self):
        min_cost = float('inf')
        key_min_item = None
        for key, cost in self.costs.items():
            if key not in self.processed:
                if cost < min_cost:
                    min_cost = cost
                    key_min_item = key
        return key_min_item

    parents = {}

    def found_parents(self, point):
        self.parents.setdefault(point, None)
        for key in self.graph.keys():
            for value in self.graph[key]:
                self.parents.setdefault(value, key)
        return self.parents

    processed = []

    def dijkstra_shortest_path(self, start_point):
        start = start_point
        self.find_costs(start)
        self.processed.append(start)
        self.way.append(start)
        node = self.find_lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                if n not in self.processed:
                    new_cost = cost + neighbors[n]
                    if self.costs[n] > new_cost:
                        self.costs[n] = new_cost
                        self.parents[n] = node
            self.processed.append(node)
            node = self.find_lowest_cost_node()
        return self.costs

    def dijkstra_get_path(self, start, end, l):
        way = [end]
        cost = l[end]
        point = end
        while cost != 0:
            way_len = self.graph[point]
            for key, w in way_len.items():
                if cost - w == l[key]:
                    cost -= w
                    point = key
                    way.append(key)
                else:
                    if point in self.graph[start] and self.graph[start][point] - cost == 0:
                        cost = 0
                        way.append(start)
        way.reverse()
        print('->'.join(way), '({})'.format(l[end]))



def main():
    g = Graph()
    g.loadfromfile('Дейкстра/2.txt')
    l = (g.dijkstra_shortest_path('x1'))
    g.dijkstra_get_path('x1', 'x2',l)


if __name__ == '__main__':
    main()
