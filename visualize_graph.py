import json
from graphviz import Digraph
import os

# Check if langgraph.json exists
if not os.path.exists("langgraph.json"):
    print("Error: langgraph.json not found. Please run services/graph.py to generate it.")
    exit(1)

# Load the graph structure from langgraph.json
try:
    with open("langgraph.json", "r") as f:
        graph_data = json.load(f)
except json.JSONDecodeError as e:
    print(f"Error: langgraph.json is invalid JSON: {e}")
    exit(1)
except Exception as e:
    print(f"Error: Failed to read langgraph.json: {e}")
    exit(1)

# Create a Graphviz Digraph
dot = Digraph(comment="LangGraph Workflow")

# Add nodes
for node in graph_data["nodes"]:
    dot.node(node["id"], label=node.get("label", node["id"]))

# Add edges
for edge in graph_data["edges"]:
    dot.edge(edge["source"], edge["target"], label=edge.get("condition", ""))

# Render the graph to a file and view it
dot.render("workflow_graph", format="png", view=True)
print("Graph rendered as workflow_graph.png")