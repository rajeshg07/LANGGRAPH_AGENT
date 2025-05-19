import uvicorn
from fastapi import FastAPI
from langgraph_example.routes.api import process_query, get_graph, app as api_app  # Import the route functions and app
from langgraph_example.services.graph import build_graph

app = FastAPI(title="LangGraph Agent")

# Include routes directly
app.post("/query")(process_query)
app.get("/graph")(get_graph)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

