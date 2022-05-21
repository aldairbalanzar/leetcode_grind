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
    for node in map:
        print(f'{node}: {map[node]}')
    return map

def bfs(start, target):
    # graph that will be traversed
    graph = create_graph()
    # queue of nodes to check connections until target is found
    queue_stack = [start]
    # keep track of already seen nodes to not queue them again
    seen = set()

    # iterate through queue as long as it is not empty
    while len(queue_stack) > 0:
        # remove node from queue because we are currently checking it's connections
        curr = queue_stack.pop(0)
        # add to seen so that we don't check connections again
        seen.add(curr)
        # iterate through every connection of that node
        for end in graph[curr]:
            # if our target is found
            if end == target:
                print(f'\nfound: {target}')
                return
            # if not found in current's connnections and has not been seen, add it to seen and queue to check it's connections
            if end not in seen:
                seen.add(end)
                queue_stack.append(end)

    # once queue is empty and target was not found
    print(f'\ntarget {target} not found')
    return

bfs('a', 'd')

