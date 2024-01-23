import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
knowledge_graph = nx.DiGraph()

# Define classes in the ontology
classes = ["Article", "MachineLearning", "DeepLearning", "DataScience"]



# Define taxonomy relationships
taxonomy_relations = [
    ("MachineLearning", "Article"),
    ("DeepLearning", "MachineLearning"),
    ("DataScience", "Article"),
]

# Add nodes to the graph
knowledge_graph.add_nodes_from(classes)

# Add edges to represent taxonomy relationships
knowledge_graph.add_edges_from(taxonomy_relations)

# Visualize the knowledge graph
pos = nx.spring_layout(knowledge_graph)
nx.draw(knowledge_graph, pos, with_labels=True, font_weight="bold", node_size=1000, node_color="skyblue")
plt.show()
