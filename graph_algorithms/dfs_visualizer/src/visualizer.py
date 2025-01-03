import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.patches import Patch

class DFSVisualizer:
    def __init__(self, graph, dfs):
        self.graph = graph
        self.dfs = dfs
        self.current_path_index = 0
        self.current_step_index = 0
        self.paths = None
        self.pos = None
        self.paused = False
        self.colors = {
            'unvisited': '#A8E6CF',  # Light mint
            'current': '#FFD3B6',     # Light orange
            'visited': '#FF8B94',     # Light red
            'path': '#FF4444'         # Bright red for edges
        }
        
    def visualize(self, paths):
        self.paths = paths
        self.pos = nx.spring_layout(self.graph.graph, seed=42)
        
        # Create two subplots - one for graph, one for stats
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, figsize=(15, 8), 
                                                      gridspec_kw={'width_ratios': [3, 1]})
        plt.gcf().canvas.mpl_connect('key_press_event', self.on_key_press)
        
        self.draw_current_state()
        plt.show()

    def draw_current_state(self):
        self.ax1.clear()
        self.ax2.clear()
        
        # Draw base graph with circular layout
        pos = nx.circular_layout(self.graph.graph)
        nx.draw(self.graph.graph, pos, ax=self.ax1, with_labels=True,
                node_size=1500, font_size=14, node_color=self.colors['unvisited'],
                edge_color='gray', width=1, font_weight='bold')
        
        if self.current_path_index < len(self.paths):
            current_path = self.paths[self.current_path_index]
            # Draw visited path
            for i in range(min(self.current_step_index, len(current_path) - 1)):
                edge = (current_path[i], current_path[i + 1])
                nx.draw_networkx_edges(self.graph.graph, pos, ax=self.ax1,
                                     edgelist=[edge], edge_color=self.colors['path'], 
                                     width=3)
                nx.draw_networkx_nodes(self.graph.graph, pos, ax=self.ax1,
                                     nodelist=[current_path[i]], 
                                     node_color=self.colors['visited'])
            
            if self.current_step_index < len(current_path):
                nx.draw_networkx_nodes(self.graph.graph, pos, ax=self.ax1,
                                     nodelist=[current_path[self.current_step_index]],
                                     node_color=self.colors['current'])
        
        self.draw_stats_panel()
        plt.draw()

    def draw_stats_panel(self):
        self.ax2.set_axis_off()
        
        # Title
        self.ax2.text(0.1, 0.95, 'DFS Path Visualization', 
                     fontsize=14, fontweight='bold')
        
        # Stats
        stats_text = [
            f"Total Paths: {len(self.paths)}",
            f"Current Path: {self.current_path_index + 1}/{len(self.paths)}",
            f"Current Step: {self.current_step_index + 1}",
            "\nControls:",
            "→ Next Step",
            "← Previous Step",
            "↑ Next Path",
            "↓ Previous Path",
            "Space: Pause/Resume",
            "R: Reset",
        ]
        
        y_pos = 0.85
        for text in stats_text:
            if text.startswith('\n'):
                y_pos -= 0.06
                text = text.strip()
            self.ax2.text(0.1, y_pos, text, fontsize=12)
            y_pos -= 0.05

        # Draw legend at bottom
        self.draw_legend_in_stats_panel()

    def draw_legend_in_stats_panel(self):
        legend_elements = [
            Patch(facecolor=self.colors['unvisited'], label='Unvisited Node'),
            Patch(facecolor=self.colors['current'], label='Current Node'),
            Patch(facecolor=self.colors['visited'], label='Visited Node'),
            Patch(facecolor=self.colors['path'], label='Path Edge')
        ]
        
        # Position legend at the bottom of stats panel
        self.ax2.legend(handles=legend_elements, 
                       loc='center',
                       bbox_to_anchor=(0.5, 0.2),
                       title='Legend',
                       frameon=True,
                       fancybox=True,
                       shadow=True)

    def on_key_press(self, event):
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
        self.current_path_index = 0
        self.current_step_index = 0
