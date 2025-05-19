# # from langgraph.graph import StateGraph, END
# # from langgraph_example.schemas.state import AgentState
# # from langgraph_example.services.nodes import hashtag_generator, trend_analyzer, default_handler

# # def build_graph():
# #     graph = StateGraph(AgentState)
# #     graph.add_node("hashtag_generator", hashtag_generator)
# #     graph.add_node("trend_analyzer", trend_analyzer)
# #     graph.add_node("default_handler", default_handler)

# #     def get_next_node(state):
# #         query = state["query"].lower()
# #         if "hashtag" in query or "hashtags" in query:
# #             return "hashtag_generator"
# #         elif "trend" in query or "trends" in query:
# #             return "trend_analyzer"
# #         return "default_handler"

# #     graph.set_entry_point("default_handler")  # Start with default to check intent
# #     graph.add_conditional_edges("default_handler", get_next_node, {
# #         "hashtag_generator": "hashtag_generator",
# #         "trend_analyzer": "trend_analyzer",
# #         "default_handler": END
# #     })
# #     graph.add_edge("hashtag_generator", END)
# #     graph.add_edge("trend_analyzer", END)

# #     return graph.compile()




# # from langgraph.graph import StateGraph, END
# # from langgraph_example.schemas.state import AgentState
# # from langgraph_example.services.nodes import hashtag_generator, trend_analyzer, default_handler
# # import json
# # import os
# # from dotenv import load_dotenv

# # load_dotenv()

# # def build_graph():
# #     graph = StateGraph(AgentState)
# #     graph.add_node("hashtag_generator", hashtag_generator)
# #     graph.add_node("trend_analyzer", trend_analyzer)
# #     graph.add_node("default_handler", default_handler)

# #     def get_next_node(state):
# #         query = state["query"].lower()
# #         if "hashtag" in query or "hashtags" in query:
# #             return "hashtag_generator"
# #         elif "trend" in query or "trends" in query:
# #             return "trend_analyzer"
# #         return "default_handler"

# #     graph.set_entry_point("default_handler")
# #     graph.add_conditional_edges("default_handler", get_next_node, {
# #         "hashtag_generator": "hashtag_generator",
# #         "trend_analyzer": "trend_analyzer",
# #         "default_handler": END
# #     })
# #     graph.add_edge("hashtag_generator", END)
# #     graph.add_edge("trend_analyzer", END)

# #     return graph.compile()

# # def export_graph_to_json():
# #     graph = build_graph()
# #     graph_structure = {
# #         "nodes": [
# #             {"id": "default_handler", "type": "function", "label": "Default Handler"},
# #             {"id": "hashtag_generator", "type": "function", "label": "Hashtag Generator"},
# #             {"id": "trend_analyzer", "type": "function", "label": "Trend Analyzer"},
# #             {"id": "end", "type": "end", "label": "End"}
# #         ],
# #         "edges": [
# #             {"source": "default_handler", "target": "hashtag_generator", "condition": "hashtag or hashtags in query"},
# #             {"source": "default_handler", "target": "trend_analyzer", "condition": "trend or trends in query"},
# #             {"source": "default_handler", "target": "end", "condition": "default"},
# #             {"source": "hashtag_generator", "target": "end"},
# #             {"source": "trend_analyzer", "target": "end"}
# #         ]
# #     }
# #     with open("langgraph.json", "w") as f:
# #         json.dump(graph_structure, f, indent=2)
# #     return graph_structure

# # if __name__ == "__main__":
# #     export_graph_to_json()


# from langgraph.graph import StateGraph, END
# from langgraph_example.schemas.state import AgentState
# from langgraph_example.services.nodes import hashtag_generator, trend_analyzer, default_handler
# import json
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def build_graph():
#     graph = StateGraph(AgentState)
#     graph.add_node("hashtag_generator", hashtag_generator)
#     graph.add_node("trend_analyzer", trend_analyzer)
#     graph.add_node("default_handler", default_handler)

#     def get_next_node(state):
#         query = state["query"].lower()
#         if "hashtag" in query or "hashtags" in query:
#             return "hashtag_generator"
#         elif "trend" in query or "trends" in query:
#             return "trend_analyzer"
#         return "default_handler"

#     graph.set_entry_point("default_handler")
#     graph.add_conditional_edges("default_handler", get_next_node, {
#         "hashtag_generator": "hashtag_generator",
#         "trend_analyzer": "trend_analyzer",
#         "default_handler": END
#     })
#     graph.add_edge("hashtag_generator", END)
#     graph.add_edge("trend_analyzer", END)

#     return graph.compile()

# def export_graph_to_json():
#     graph = build_graph()
#     graph_structure = {
#         "nodes": [
#             {"id": "default_handler", "type": "function", "label": "Default Handler"},
#             {"id": "hashtag_generator", "type": "function", "label": "Hashtag Generator"},
#             {"id": "trend_analyzer", "type": "function", "label": "Trend Analyzer"},
#             {"id": "end", "type": "end", "label": "End"}
#         ],
#         "edges": [
#             {"source": "default_handler", "target": "hashtag_generator", "condition": "hashtag or hashtags in query"},
#             {"source": "default_handler", "target": "trend_analyzer", "condition": "trend or trends in query"},
#             {"source": "default_handler", "target": "end", "condition": "default"},
#             {"source": "hashtag_generator", "target": "end"},
#             {"source": "trend_analyzer", "target": "end"}
#         ]
#     }
#     with open("langgraph.json", "w") as f:
#         json.dump(graph_structure, f, indent=2)
#     return graph_structure

# if __name__ == "__main__":
#     export_graph_to_json()











from langgraph.graph import StateGraph, END
from langgraph_example.schemas.state import AgentState
from langgraph_example.services.nodes import intent_detector, hashtag_generator, trend_analyzer, llm_handler, response_validator
import json
import os
from dotenv import load_dotenv

load_dotenv()

def build_graph():
    graph = StateGraph(AgentState)
    
    # Add nodes
    graph.add_node("intent_detector", intent_detector)
    graph.add_node("hashtag_generator", hashtag_generator)
    graph.add_node("trend_analyzer", trend_analyzer)
    graph.add_node("llm_handler", llm_handler)
    graph.add_node("response_validator", response_validator)

    # Define routing functions
    def route_by_intent(state):
        intent = state.get("intent", "general")
        if intent == "hashtags":
            return "hashtag_generator"
        elif intent == "trends":
            return "trend_analyzer"
        else:
            return "llm_handler"

    def route_after_validation(state):
        if state.get("is_valid", False):
            return "end"
        else:
            return "intent_detector"

    # Set entry point
    graph.set_entry_point("intent_detector")

    # Add conditional edges
    graph.add_conditional_edges("intent_detector", route_by_intent, {
        "hashtag_generator": "hashtag_generator",
        "trend_analyzer": "trend_analyzer",
        "llm_handler": "llm_handler"
    })

    # Route each handler to the validator
    graph.add_edge("hashtag_generator", "response_validator")
    graph.add_edge("trend_analyzer", "response_validator")
    graph.add_edge("llm_handler", "response_validator")

    # Add conditional edge for validation loop
    graph.add_conditional_edges("response_validator", route_after_validation, {
        "intent_detector": "intent_detector",
        "end": END
    })

    return graph.compile()

def export_graph_to_json():
    graph = build_graph()
    graph_structure = {
        "nodes": [
            {"id": "intent_detector", "type": "function", "label": "Intent Detector"},
            {"id": "hashtag_generator", "type": "function", "label": "Hashtag Generator"},
            {"id": "trend_analyzer", "type": "function", "label": "Trend Analyzer"},
            {"id": "llm_handler", "type": "function", "label": "LLM Handler"},
            {"id": "response_validator", "type": "function", "label": "Response Validator"},
            {"id": "end", "type": "end", "label": "End"}
        ],
        "edges": [
            {"source": "intent_detector", "target": "hashtag_generator", "condition": "intent = hashtags"},
            {"source": "intent_detector", "target": "trend_analyzer", "condition": "intent = trends"},
            {"source": "intent_detector", "target": "llm_handler", "condition": "intent = general"},
            {"source": "hashtag_generator", "target": "response_validator"},
            {"source": "trend_analyzer", "target": "response_validator"},
            {"source": "llm_handler", "target": "response_validator"},
            {"source": "response_validator", "target": "intent_detector", "condition": "response invalid"},
            {"source": "response_validator", "target": "end", "condition": "response valid"}
        ]
    }
    with open("langgraph.json", "w") as f:
        json.dump(graph_structure, f, indent=2)
    return graph_structure

if __name__ == "__main__":
    export_graph_to_json()