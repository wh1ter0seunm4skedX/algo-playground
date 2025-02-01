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
    },
    {
        'name': 'Graph 2',
        'graph': {
            'A': {'B': 3, 'C': 1, 'D': 2},
            'B': {'A': 3, 'E': 4, 'F': 5},
            'C': {'A': 1, 'G': 2},
            'D': {'A': 2, 'H': 3},
            'E': {'B': 4, 'I': 1},
            'F': {'B': 5, 'J': 2},
            'G': {'C': 2, 'H': 1},
            'H': {'D': 3, 'G': 1},
            'I': {'E': 1, 'J': 3},
            'J': {'F': 2, 'I': 3}
        }
    },
    {
        'name': 'Graph 3',
        'graph': {
            'X': {'Y': 4, 'Z': 2, 'W': 3},
            'Y': {'X': 4, 'V': 1, 'U': 5},
            'Z': {'X': 2, 'T': 6},
            'W': {'X': 3, 'S': 2},
            'V': {'Y': 1, 'T': 3},
            'U': {'Y': 5, 'S': 1},
            'T': {'V': 3, 'Z': 6},
            'S': {'W': 2, 'U': 1}
        }
    }
]

def choose_graph():
    print("Choose a graph:")
    for i, option in enumerate(graph_options):
        print(f"{i + 1}. {option['name']}")
    choice = int(input("Enter the number of the graph you want to visualize: ")) - 1
    return graph_options[choice]['graph']
