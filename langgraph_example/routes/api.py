from fastapi import FastAPI
from langgraph_example.services.graph import build_graph, export_graph_to_json
from langgraph_example.schemas.state import AgentState
import logging
from langsmith import traceable

# Create the app instance (no routes defined here)
app = FastAPI()

# Initialize graph
graph = build_graph()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# In-memory conversation history
conversation_history = []

@traceable
async def process_query(query: str):
    state: AgentState = {
        "query": query,
        "intent": "",
        "response": "",
        "hashtags": [],
        "trends": [],
        "logs": [],
        "flags": {},
        "is_valid": False,
        "retry_count": 0
    }
    state["logs"].append(f"Received query: {query}")
    logger.info(f"Processing query: {query}")

    if conversation_history:
        context = "Previous conversation:\n" + "\n".join([f"Q: {entry['query']} A: {entry['response']}" for entry in conversation_history[-2:]])
        state["query"] = f"{context}\nCurrent query: {query}"

    result = await graph.ainvoke(state)
    result["logs"].append(f"Response generated: {result['response']}")
    logger.info(f"Response: {result['response']}")

    conversation_history.append({"query": query, "response": result["response"]})

    return {
        "response": result["response"],
        "hashtags": result["hashtags"],
        "trends": result["trends"],
        "logs": result["logs"],
        "flags": result["flags"],
        "conversation_history": conversation_history[-2:]
    }

async def get_graph():
    return export_graph_to_json()

