graph_options = [
    {
        'name': 'Graph 1',
        'graph': {
            'A': {'B': 2, 'D': 1, 'E': 3},
            'B': {'A': 2, 'C': 4, 'F': 5},
            'C': {'B': 4, 'D': 2, 'G': 1},
            'D': {'A': 1, 'C': 2, 'H': 4},
            'E': {'A': 3, 'F': 1, 'I': 2},
            'F': {'B': 5, 'E': 1, 'J': 3},
            'G': {'C': 1, 'H': 2},
            'H': {'D': 4, 'G': 2, 'J': 2},
            'I': {'E': 2, 'J': 1},
            'J': {'F': 3, 'H': 2, 'I': 1}
        }
    }
]

def choose_graph():
    return graph_options[0]['graph']

graph = choose_graph()