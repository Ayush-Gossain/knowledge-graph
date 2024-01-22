# 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

import openai
import networkx as nx
import matplotlib.pyplot as plt

# Set up your OpenAI API key
openai.api_key = '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'

# Use GPT-3 to generate textual descriptions
descriptions = [
    "Python is a programming language.",
    "Data Science involves analyzing and interpreting complex data sets.",
    "Machine Learning is a field of artificial intelligence that focuses on building systems that learn from data.",
    "Graph Theory is the study of graphs, which are mathematical structures used to model pairwise relations between objects.",
    "NetworkX is a Python library for creating, analyzing, and visualizing complex networks.",
]

# Create a directed graph
knowledge_graph = nx.DiGraph()

# Add nodes and edges based on GPT-3 generated descriptions
for description in descriptions:
    entities = openai.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=f"Extract entities from the following text: '{descriptions}'",
        max_tokens=150
    )['choices'][0]['message']['content'].split(',')

    entities = [entity.strip() for entity in entities]

    for entity in entities:
        knowledge_graph.add_node(entity)

    for source_entity in entities:
        for target_entity in entities:
            if source_entity != target_entity:
                knowledge_graph.add_edge(source_entity, target_entity)

# Draw the graph
pos = nx.spring_layout(knowledge_graph)
nx.draw(knowledge_graph, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", edge_color="gray", linewidths=1, arrowsize=20)

# Show the graph
plt.show()
