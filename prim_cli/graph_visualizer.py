import networkx as nx
import matplotlib.pyplot as plt

def display_graph(edges, title):
    plt.clf()
    
    G = nx.Graph()
    
    # Add edges with weights
    for node1, node2, weight in edges:
        G.add_edge(node1, node2, weight=weight)
    
    # Get positions for the nodes
    pos = nx.spring_layout(G)  # You can experiment with other layouts
    
    # Draw the nodes and edges
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=12, font_weight="bold")
    edge_labels = {(node1, node2): f"{weight}" for node1, node2, weight in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color="red")
    
    plt.title(title)
    plt.show(block=True) 
    plt.close() 
