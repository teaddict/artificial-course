# graph is in adjacent list representation
graph = {
        'a': ['b', 'e'],
        'b': ['d', 'c'],
        'c': ['b','d'],
        'd': ['c', 'b'],
        'e': ['f']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        print(path)
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

print ("FOUND WAY: " + str(bfs(graph, 'a', 'f')))