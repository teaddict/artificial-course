# graph is in adjacent list representation
graph = {
        'a': ['b', 'e'],
        'b': ['d', 'c'],
        'c': ['b','d'],
        'd': ['c', 'b'],
        'e': ['f']
        }
def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        print(path)
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                paths += find_all_paths(graph, node, end, path)
        return paths

print ("FOUND WAY: " + str(find_all_paths(graph, 'a', 'f')))