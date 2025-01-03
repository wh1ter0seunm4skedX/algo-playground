import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import time
import sys

class GraphVisualizer:
    terminate_program = False  # Class variable to track termination
    
    def __init__(self, graph):
        self.G = nx.Graph()
        self.graph = graph
        self._build_networkx_graph()
        self.pos = nx.spring_layout(self.G)
        self.speed = 1.0  # Animation speed control
        self.paused = False
        self.current_frame = 0
        self.frames = []
        self.step_count = 0
        self.anim = None
        self.current_frame_idx = 0
        self.should_continue = False  # Instance variable for "Next" control
    
    def _build_networkx_graph(self):
        for vertex in self.graph.get_vertices():
            self.G.add_node(vertex)
            for neighbor in self.graph.get_neighbors(vertex):
                self.G.add_edge(vertex, neighbor)
    
    def set_speed(self, speed):
        """Control animation speed (0.5 = slower, 2.0 = faster)"""
        self.speed = speed
    
    def visualize_traversal(self, traversal_generator, title="Graph Traversal"):
        fig = plt.figure(figsize=(15, 8))
        fig.canvas.manager.set_window_title('Graph Algorithm Visualizer - ' + title)  # Add this line
        
        # Create main graph subplot with adjusted size to make room for buttons
        ax_graph = plt.subplot2grid((1, 5), (0, 0), colspan=4)
        ax_info = plt.subplot2grid((1, 5), (0, 4))
        
        # Add buttons with better positioning, including next and exit buttons
        ax_back = plt.axes([0.4, 0.05, 0.08, 0.04])
        ax_start = plt.axes([0.5, 0.05, 0.08, 0.04])
        ax_pause = plt.axes([0.6, 0.05, 0.08, 0.04])
        ax_forward = plt.axes([0.7, 0.05, 0.08, 0.04])
        ax_next = plt.axes([0.8, 0.05, 0.08, 0.04])
        ax_exit = plt.axes([0.9, 0.05, 0.08, 0.04])
        
        btn_back = Button(ax_back, '<')
        btn_start = Button(ax_start, '|<<')
        btn_pause = Button(ax_pause, '||')
        btn_forward = Button(ax_forward, '>')
        btn_next = Button(ax_next, '>>')
        btn_exit = Button(ax_exit, 'X')
        
        btn_next.color = 'lightgreen'
        btn_exit.color = 'lightcoral'
        
        self.frames = list(traversal_generator)
        self.current_frame_idx = 0
        self.step_count = 0
        self.paused = False  # Start playing immediately
        
        # Initialize as paused
        self.paused = True
        
        def update_frame(frame_idx):
            if frame_idx >= len(self.frames) or frame_idx < 0:
                return
            
            frame = self.frames[frame_idx]
            ax_graph.clear()
            ax_info.clear()
            
            current_vertex, visited, queue = frame
            
            # Draw edges with different colors
            edge_colors = []
            for edge in self.G.edges():
                if edge[0] in visited and edge[1] in visited:
                    edge_colors.append('green')
                else:
                    edge_colors.append('gray')
            
            nx.draw_networkx_edges(self.G, self.pos, 
                                 edge_color=edge_colors, 
                                 ax=ax_graph)
            
            # Draw nodes
            node_colors = []
            for node in self.G.nodes():
                if node == current_vertex:
                    node_colors.append('red')
                elif node in visited:
                    node_colors.append('green')
                elif node in queue:
                    node_colors.append('#FFD700') 
                else:
                    node_colors.append('lightblue')
            
            nx.draw_networkx_nodes(self.G, self.pos, 
                                 node_color=node_colors, 
                                 ax=ax_graph)
            nx.draw_networkx_labels(self.G, self.pos, ax=ax_graph)
 
            # Update information panel
            ax_info.text(0.1, 0.95, f"Step: {self.step_count}", fontsize=10)
            ax_info.text(0.1, 0.85, f"Current: {current_vertex}", fontsize=10)
            ax_info.text(0.1, 0.75, f"Visited: {visited}", fontsize=10)
            ax_info.text(0.1, 0.55, f"{queue}", fontsize=10)
            
            # Determine if this is BFS or DFS based on the title
            structure_name = "Queue" if "BFS" in title else "Stack"
            
            legend_text = (
                "Color Legend:\n"
                "🔴 Red: Current vertex\n"
                "🟢 Green: Visited vertices\n"
                f"🟡 Yellow: In {structure_name}\n"
                "🔵 Blue: Unvisited vertices\n"
                "\nEdges:\n"
                "─── Green: Traversed\n"
                "─── Gray: Unexplored"
            )
            
            ax_info.text(0.1, 0.2, legend_text, 
                        fontsize=9,
                        bbox=dict(facecolor='white', 
                                alpha=0.8,
                                edgecolor='gray',
                                boxstyle='round'))
            
            # Update structure label
            ax_info.text(0.1, 0.65, f"{structure_name}:", fontsize=10)
            
            ax_info.axis('off')
            ax_graph.set_title(f"{title} - Step {frame_idx}")
            
            self.current_frame_idx = frame_idx
            self.step_count = frame_idx
        
        def update(frame):
            if not self.paused:
                if self.current_frame_idx < len(self.frames):
                    update_frame(self.current_frame_idx)
                    self.current_frame_idx += 1
                elif self.current_frame_idx == len(self.frames):
                    # Show completion dialog
                    self.paused = True
                    btn_pause.label.set_text('▶')
                    plt.annotate('Traversal Complete!', 
                                xy=(0.5, 0.5), 
                                xycoords='figure fraction',
                                bbox=dict(boxstyle='round,pad=0.5', 
                                        fc='lightgreen', 
                                        alpha=0.7),
                                fontsize=12,
                                ha='center')
                    self.current_frame_idx += 1  # Prevent multiple dialogs
        
        def on_pause(event):
            self.paused = not self.paused
            btn_pause.label.set_text('▶' if self.paused else '||')
            
        def on_back(event):
            self.paused = True
            btn_pause.label.set_text('▶')
            new_idx = max(0, self.current_frame_idx - 1)
            update_frame(new_idx)
            
        def on_forward(event):
            self.paused = True
            btn_pause.label.set_text('▶')
            new_idx = min(len(self.frames) - 1, self.current_frame_idx + 1)
            update_frame(new_idx)
        
        def on_next(event):
            self.should_continue = True
            plt.close(fig)
        
        def on_exit(event):
            GraphVisualizer.terminate_program = True
            plt.close(fig)
        
        def on_start(event):
            self.paused = True
            btn_pause.label.set_text('▶')
            self.current_frame_idx = 0
            update_frame(0)

        btn_pause.on_clicked(on_pause)
        btn_back.on_clicked(on_back)
        btn_forward.on_clicked(on_forward)
        btn_next.on_clicked(on_next)
        btn_exit.on_clicked(on_exit)
        btn_start.on_clicked(on_start)
        
        interval = 1000 / self.speed
        self.anim = FuncAnimation(
            fig, 
            update, 
            frames=None,
            interval=interval, 
            repeat=False,
            cache_frame_data=False  # Prevent caching warning
        )
        
        # Start with play button
        btn_pause.label.set_text('||')
        
        plt.show()
        
        return not GraphVisualizer.terminate_program and self.should_continue
