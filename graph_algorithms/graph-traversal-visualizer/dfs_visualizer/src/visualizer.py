import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Patch, Rectangle

class DFSVisualizer:
    def __init__(self, graph, dfs, randomize_callback=None, new_graph_callback=None):
        self.graph = graph
        self.dfs = dfs
        self.current_path_index = 0
        self.current_step_index = 0
        self.paths = None
        self.pos = None
        self.paused = False
        self.colors = {
            'unvisited': '#A8E6CF',    # Light mint
            'current': '#FFD3B6',       # Light orange
            'visited': '#FF8B94',       # Light red
            'path': '#FF4444',          # Bright red for edges
            'edge': 'lightgray',        # Default edges
            'tree': '#2ecc71',          # Green for tree edges
            'back': '#e74c3c',          # Red for back edges
            'forward': '#3498db',       # Blue for forward edges
            'cross': '#9b59b6'          # Purple for cross edges
        }
        self.stack = []
        self.visited_nodes = set()
        self.randomize_callback = randomize_callback
        self.new_graph_callback = new_graph_callback
        
    def visualize(self, paths):
        self.paths = paths
        self.pos = nx.spring_layout(self.graph.graph, k=2, iterations=50)
        
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(15, 8), 
                                                      gridspec_kw={'width_ratios': [2, 1]})
        plt.gcf().canvas.mpl_connect('key_press_event', self.on_key_press)
        
        self.draw_current_state()
        plt.show()

    def draw_current_state(self):
        self.ax1.clear()
        self.ax2.clear()
        
        # Draw base graph with spring layout
        nx.draw(self.graph.graph, self.pos, ax=self.ax1, with_labels=True,
                node_size=1500, font_size=14, node_color=self.colors['unvisited'],
                edge_color=self.colors['edge'], width=1, font_weight='bold')
        
        if self.current_path_index < len(self.paths):
            current_path = self.paths[self.current_path_index]
            
            # Update visited nodes and stack for visualization
            self.visited_nodes = set(current_path[:self.current_step_index + 1])
            self.stack = current_path[:self.current_step_index + 1]
            
            # Draw visited path
            for i in range(min(self.current_step_index, len(current_path) - 1)):
                edge = (current_path[i], current_path[i + 1])
                nx.draw_networkx_edges(self.graph.graph, self.pos, ax=self.ax1,
                                     edgelist=[edge], edge_color=self.colors['path'], 
                                     width=3)
            
            # Draw visited nodes
            if self.visited_nodes:
                nx.draw_networkx_nodes(self.graph.graph, self.pos, ax=self.ax1,
                                     nodelist=list(self.visited_nodes),
                                     node_color=self.colors['visited'])
            
            # Draw current node
            if self.current_step_index < len(current_path):
                nx.draw_networkx_nodes(self.graph.graph, self.pos, ax=self.ax1,
                                     nodelist=[current_path[self.current_step_index]],
                                     node_color=self.colors['current'])
        
        self.draw_dfs_state_panel()
        plt.draw()

    def draw_dfs_state_panel(self):
        self.ax2.set_axis_off()
        
        # Title with instructions
        title_text = (f'DFS Visualization\nPath {self.paths[0][0]} → {self.paths[0][-1]}\n'
                     f'(N: New path | G: New graph)')
        self.ax2.text(0.1, 0.95, title_text, fontsize=14, fontweight='bold')
        
        # Draw DFS internal state
        y_pos = 0.85
        
        # Stack visualization
        self.ax2.text(0.1, y_pos, 'Stack:', fontsize=12, fontweight='bold')
        y_pos -= 0.05
        for node in reversed(self.stack):
            self.ax2.add_patch(Rectangle((0.1, y_pos), 0.2, 0.04, 
                                       facecolor=self.colors['current']))
            self.ax2.text(0.2, y_pos + 0.02, str(node), ha='center')
            y_pos -= 0.05
        
        # Visited set visualization
        y_pos -= 0.1
        self.ax2.text(0.1, y_pos, 'Visited:', fontsize=12, fontweight='bold')
        y_pos -= 0.05
        visited_str = ', '.join(map(str, sorted(self.visited_nodes)))
        self.ax2.text(0.1, y_pos, f'{{{visited_str}}}', fontsize=12)
        
        # Path information
        y_pos -= 0.1
        self.ax2.text(0.1, y_pos, 
                      f'Path {self.current_path_index + 1}/{len(self.paths)}',
                      fontsize=12)
        
        # Draw legend at bottom
        self.draw_legend_in_stats_panel()

    def draw_legend_in_stats_panel(self):
        legend_elements = [
            Patch(facecolor=self.colors['unvisited'], label='Unvisited Node'),
            Patch(facecolor=self.colors['current'], label='Current Node'),
            Patch(facecolor=self.colors['visited'], label='Visited Node'),
            Patch(facecolor=self.colors['path'], label='Visited Path'),
        ]
        
        # Position legend at the bottom of stats panel
        self.ax2.legend(handles=legend_elements, 
                       loc='center',
                       bbox_to_anchor=(0.5, 0.2),
                       title='Legend',
                       frameon=True,
                       fancybox=True,
                       shadow=True,
                       ncol=1)

    def on_key_press(self, event):
        if event.key == 'g' and self.new_graph_callback:
            # Generate new graph and update visualization
            new_paths = self.new_graph_callback()
            if new_paths:
                self.paths = new_paths
                # Graph and DFS references are already updated by the callback
                self.reset()
                self.draw_current_state()
            return
            
        if event.key == 'n' and self.randomize_callback:
            # Call the randomize callback and update visualization
            new_paths = self.randomize_callback()
            if new_paths:
                self.paths = new_paths
                # Graph and DFS references are already updated by the callback
                self.reset()
                self.draw_current_state()
            return

        if event.key == 'right':
            self.next_step()
        elif event.key == 'left':
            self.previous_step()
        elif event.key == 'up':
            self.next_path()
        elif event.key == 'down':
            self.previous_path()
        elif event.key == ' ':
            self.paused = not self.paused
        elif event.key == 'r':
            self.reset()
        
        self.draw_current_state()

    def next_step(self):
        if self.current_path_index < len(self.paths):
            if self.current_step_index < len(self.paths[self.current_path_index]):
                self.current_step_index += 1

    def previous_step(self):
        if self.current_step_index > 0:
            self.current_step_index -= 1

    def next_path(self):
        if self.current_path_index < len(self.paths) - 1:
            self.current_path_index += 1
            self.current_step_index = 0

    def previous_path(self):
        if self.current_path_index > 0:
            self.current_path_index -= 1
            self.current_step_index = 0

    def reset(self):
        """Reset visualization state"""
        self.current_path_index = 0
        self.current_step_index = 0
        self.visited_nodes.clear()
        self.stack.clear()
        # Recalculate layout when resetting
        self.pos = nx.spring_layout(self.graph.graph, k=2, iterations=50)

    def update_graph_and_dfs(self, graph, dfs):
        """Update the graph and DFS references and reset visualization state"""
        self.graph = graph
        self.dfs = dfs
        self.current_path_index = 0
        self.current_step_index = 0
        self.visited_nodes.clear()
        self.stack.clear()
        # Recalculate layout for new graph
        self.pos = nx.spring_layout(self.graph.graph, k=2, iterations=50)
