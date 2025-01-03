import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.widgets import Button

class DFSVisualizer:
    def __init__(self, graph, dfs):
        self.graph = graph
        self.dfs = dfs
        self.current_path_index = 0
        self.current_step_index = 0
        self.paths = None
        self.pos = None
        self.paused = False
        
    def visualize(self, paths):
        self.paths = paths
        self.pos = nx.spring_layout(self.graph.graph, seed=42)
        plt.figure(figsize=(10, 8))
        
        # Add key event handlers
        plt.gcf().canvas.mpl_connect('key_press_event', self.on_key_press)
        
        # Initial display
        self.draw_current_state()
        self.add_instructions()
        plt.show()

    def draw_current_state(self):
        plt.clf()
        
        # Draw base graph
        nx.draw(self.graph.graph, self.pos, with_labels=True, 
                node_size=2000, font_size=16, node_color='lightblue')
        
        if self.current_path_index < len(self.paths):
            current_path = self.paths[self.current_path_index]
            # Draw visited path
            for i in range(min(self.current_step_index, len(current_path) - 1)):
                edge = (current_path[i], current_path[i + 1])
                nx.draw_networkx_edges(self.graph.graph, self.pos, 
                                     edgelist=[edge], edge_color='red', width=3)
                nx.draw_networkx_nodes(self.graph.graph, self.pos, 
                                     nodelist=[current_path[i]], node_color='orange')
            
            if self.current_step_index < len(current_path):
                nx.draw_networkx_nodes(self.graph.graph, self.pos, 
                                     nodelist=[current_path[self.current_step_index]], 
                                     node_color='yellow')
        
        self.add_instructions()
        plt.draw()

    def add_instructions(self):
        plt.title("DFS Path Visualization\n" +
                 "Right Arrow: Next Step | Left Arrow: Previous Step\n" +
                 "Up Arrow: Next Path | Down Arrow: Previous Path\n" +
                 "Space: Pause/Resume | R: Reset\n" +
                 f"Path {self.current_path_index + 1}/{len(self.paths)}, " +
                 f"Step {self.current_step_index + 1}")

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
