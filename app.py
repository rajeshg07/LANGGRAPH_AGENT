import gradio as gr
import httpx
import json

FASTAPI_URL = "http://0.0.0.0:8000/query"
CLEAR_HISTORY_URL = "http://0.0.0.0:8000/clear_history"

async def query_agent(user_query):
    if not user_query.strip():
        return "Please enter a query.", "", "", "", ""

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(FASTAPI_URL, json={"query": user_query})
            response.raise_for_status()
            result = response.json()

        response_text = result.get("response", "No response received.")
        hashtags = ", ".join(result.get("hashtags", [])) or "No hashtags generated."
        trends = ", ".join(result.get("trends", [])) or "No trends analyzed."
        logs = "\n".join(result.get("logs", [])) or "No logs available."
        conversation_history = "\n".join(
            [f"Q: {entry['query']} A: {entry['response']}" for entry in result.get("conversation_history", [])]
        ) or "No conversation history."

        return response_text, hashtags, trends, logs, conversation_history

    except httpx.HTTPStatusError as e:
        return f"Error: Failed to fetch response from backend. Status: {e.response.status_code}", "", "", "", ""
    except Exception as e:
        return f"Error: {str(e)}", "", "", "", ""

async def clear_history():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(CLEAR_HISTORY_URL)
            response.raise_for_status()
            return "Conversation history cleared.", "", "", "", ""
    except Exception as e:
        return f"Error clearing history: {str(e)}", "", "", "", ""

with gr.Blocks(title="LangGraph Agent Interface") as demo:
    gr.Markdown("# LangGraph Agent Interface")
    gr.Markdown("Interact with the LangGraph agent to generate hashtags, analyze trends, or get general answers.")
    gr.Markdown("### Example Queries:")
    gr.Markdown("- provide some hashtags for my instagram reel\n- show me the latest trends\n- what is digital marketing?")

    with gr.Row():
        query_input = gr.Textbox(
            label="Enter your query",
            placeholder="e.g., 'provide some hashtags for my instagram reel'"
        )
        with gr.Column():
            submit_button = gr.Button("Submit")
            clear_button = gr.Button("Clear History")

    with gr.Row():
        with gr.Column():
            response_output = gr.Textbox(label="Response", interactive=False)
        with gr.Column():
            hashtags_output = gr.Textbox(label="Hashtags", interactive=False)
            trends_output = gr.Textbox(label="Trends", interactive=False)

    with gr.Row():
        logs_output = gr.Textbox(label="Logs", interactive=False)
        history_output = gr.Textbox(label="Conversation History", interactive=False)

    submit_button.click(
        fn=query_agent,
        inputs=query_input,
        outputs=[response_output, hashtags_output, trends_output, logs_output, history_output]
    )
    clear_button.click(
        fn=clear_history,
        inputs=None,
        outputs=[response_output, hashtags_output, trends_output, logs_output, history_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)