import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
knowledge_graph = nx.DiGraph()

# Add nodes and edges to the graph
knowledge_graph.add_node("Python")
knowledge_graph.add_node("Data Science")
knowledge_graph.add_node("Machine Learning")
knowledge_graph.add_node("Graph Theory")
knowledge_graph.add_node("NetworkX")

knowledge_graph.add_edge("Python", "Data Science")
knowledge_graph.add_edge("Python", "Machine Learning")
knowledge_graph.add_edge("Data Science", "Machine Learning")
knowledge_graph.add_edge("Data Science", "Graph Theory")
knowledge_graph.add_edge("Machine Learning", "NetworkX")

# Draw the graph
pos = nx.spring_layout(knowledge_graph)
nx.draw(knowledge_graph, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, arrowsize=20)

# Show the graph
plt.show()
