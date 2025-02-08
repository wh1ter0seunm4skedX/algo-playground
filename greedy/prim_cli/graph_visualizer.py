import networkx as nx
import matplotlib.pyplot as plt

def display_graph(edges, title, mst_edges=None):
    G = nx.Graph()
    
    # Add all edges with weights
    for node1, node2, weight in edges:
        G.add_edge(node1, node2, weight=weight)
    
    # Set a fixed seed to ensure the layout is always the same
    pos = nx.spring_layout(G, seed=42) 
    
    # Draw the nodes and edges
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=12, font_weight="bold")
    
    # Draw all edges in default color
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="gray", width=1.5)

    # Highlight the MST edges in bold
    if mst_edges:
        nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color="red", width=3.0)
    
    # Add edge labels
    edge_labels = {(node1, node2): f"{weight}" for node1, node2, weight in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10, font_color="black")
    
    plt.title(title)
    plt.show(block=True)
    plt.close()
