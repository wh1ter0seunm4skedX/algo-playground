import networkx as nx
import matplotlib.pyplot as plt

def visualize_cut(G, pos, set_S, set_T, cut_value, title):
    plt.clf()
    
    # Color nodes based on their partition
    node_colors = ['red' if node in set_S else 'blue' for node in G.nodes()]
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
    
    # Draw edges with capacities
    edge_labels = {(u, v): d['capacity'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
    
    plt.title(f"{title}\nCut Value: {cut_value}")
    plt.draw()

def interactive_cuts(G):
    # Get minimum cut
    source, sink = 'S', 'T'
    min_cut_value, (min_set_S, min_set_T) = nx.minimum_cut(G, source, sink)
    
    # Generate 3 random cuts
    random_cuts = [random_cut(G) for _ in range(3)]
    cuts = [(min_cut_value, (min_set_S, min_set_T))] + random_cuts
    cut_names = ["Minimum Cut"] + [f"Random Cut {i+1}" for i in range(3)]
    
    # Setup visualization
    fig = plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    current_cut = [0]  # Using list to allow modification in nested function
    
    def show_current_cut():
        plt.clf()
        cut_value, (set_S, set_T) = cuts[current_cut[0]]
        
        # Color nodes based on their partition
        node_colors = ['red' if node in set_S else 'blue' for node in G.nodes()]
        
        # Draw nodes and edges
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=700)
        edge_labels = {(u, v): d['capacity'] for u, v, d in G.edges(data=True)}
        nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
        
        plt.title(f"{cut_names[current_cut[0]]}\nCut Value: {cut_value}\n(Use Left/Right arrow keys to navigate)")
        plt.draw()
    
    def on_key_press(event):
        if event.key == 'right' and current_cut[0] < len(cuts) - 1:
            current_cut[0] += 1
            show_current_cut()
        elif event.key == 'left' and current_cut[0] > 0:
            current_cut[0] -= 1
            show_current_cut()
    
    # Register keyboard listener
    fig.canvas.mpl_connect('key_press_event', on_key_press)
    
    # Show initial cut
    show_current_cut()
    plt.show()

def max_flow_min_cut():
    # Create a directed graph
    G = nx.DiGraph()
    
    # Add edges with capacities
    edges = [
        ('S', 'A', 10), ('S', 'B', 5), ('S', 'C', 15),
        ('A', 'B', 4), ('A', 'D', 9), ('A', 'E', 15),
        ('B', 'C', 4), ('B', 'E', 8),
        ('C', 'F', 16),
        ('D', 'E', 15), ('D', 'T', 10),
        ('E', 'F', 15), ('E', 'T', 10),
        ('F', 'T', 10)
    ]
    
    for u, v, capacity in edges:
        G.add_edge(u, v, capacity=capacity)
    
    # Compute max flow using Edmonds-Karp algorithm
    source, sink = 'S', 'T'
    flow_value, flow_dict = nx.maximum_flow(G, source, sink)
    
    # Compute min cut
    cut_value, (set_S, set_T) = nx.minimum_cut(G, source, sink)
    
    # Print results
    print(f"Max Flow: {flow_value}")
    print(f"Min Cut Value: {cut_value}")
    print(f"Min Cut Partition: {set_S}, {set_T}")

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
    
    # Draw edges with capacities
    edge_labels = {(u, v): d['capacity'] for u, v, d in G.edges(data=True)}
    nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    plt.title("Max Flow Min Cut Graph Representation")
    # plt.show()  # Commented out to avoid showing the plot here
    
    return G, flow_value, cut_value, set_S, set_T

def random_cut(G):
    import random
    nodes = list(G.nodes())
    nodes.remove('S')  # Remove source
    nodes.remove('T')  # Remove sink
    
    # Randomly split remaining nodes
    random.shuffle(nodes)
    split_point = random.randint(1, len(nodes)-1)
    set_S = {'S'} | set(nodes[:split_point])
    set_T = {'T'} | set(nodes[split_point:])
    
    # Calculate cut value
    cut_value = sum(G[u][v]['capacity'] for u in set_S for v in set_T if G.has_edge(u, v))
    return cut_value, (set_S, set_T)

def compare_cuts(G):
    # Get minimum cut
    source, sink = 'S', 'T'
    min_cut_value, (min_set_S, min_set_T) = nx.minimum_cut(G, source, sink)
    
    print(f"\nMinimum Cut Value: {min_cut_value}")
    print(f"Minimum Cut Partition: {min_set_S}, {min_set_T}")
    
    # Perform 3 random cuts
    print("\nRandom Cuts:")
    for i in range(3):
        cut_value, (set_S, set_T) = random_cut(G)
        print(f"Random Cut {i+1} Value: {cut_value}")
        print(f"Random Cut {i+1} Partition: {set_S}, {set_T}")

if __name__ == "__main__":
    G, flow_value, cut_value, set_S, set_T = max_flow_min_cut()
    interactive_cuts(G)
