nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
grid = [
    ['a', 'e'],
    ['a', 'd'],
    ['d', 'c'],
    ['d', 'h'],
    ['d', 'i'],
    ['f', 'e'],
    ['f', 'b'],
    ['f', 'k'],
    ['f', 'g'],
    ['k', 'b']
]
map = {}

# adds node to graph
def add_node(node):
    map[node] = []

# creates connection between nodes
def add_edge(start, end):
    map[start].append(end)
    map[end].append(start)

#creates a graph with node connections and returns it for later traversal
def create_graph():
    for node in nodes:
        add_node(node)
    for conn in grid:
        add_edge(conn[0], conn[1])
    
    return map

def dfs(start, target, seen = set()):
    print(f'node: {start}')
    # graph that will be traversed
    graph = create_graph()
    # add start to seen since we're currently checking connections
    seen.add(start)
    for end in graph[start]:
        if end == target:
            print(f'found: {target} in {len(seen)} steps\n')
            return
        if end not in seen:
            dfs(end, target, seen)

dfs('a', 'b')