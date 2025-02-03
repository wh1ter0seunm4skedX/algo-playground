def visualize_decisions(decisions, ax):
    ax.clear()
    y = 1.0  # Starting position for displaying text
    for decision in decisions:
        ax.text(0.05, y, decision, fontsize=10, family='monospace', verticalalignment='top')
        y -= 0.1
    ax.set_title("Decision Analysis")
    ax.axis('off')
