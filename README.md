
---

# **LangGraph Agent**

A modular AI agent built with LangGraph to handle user queries, generate hashtags, analyze trends, and provide general responses using a FastAPI backend and Gradio interface.

---

## **Requirements**

* Python 3.9+
* FastAPI
* Langchain
* Langgraph
* OpenAI API key (for GPT-4o-mini)
* SerpAPI key (optional, for hashtag generation)

---

## **Overview**

This project leverages **LangGraph**, a framework for building stateful, multi-agent systems, to create an AI agent that processes user queries. The agent uses an LLM (via OpenAI's gpt-4o-mini) for intent detection and response generation, with optional SerpApi integration for real-time data.

### **Key Features**

* **Intent Detection**: Classifies queries into `hashtags`, `trends`, or `general` using an LLM.
* **Hashtag Generation**: Generates trending hashtags for platforms like Instagram or TikTok using SerpApi or the LLM.
* **Trend Analysis**: Fetches current social media trends via SerpApi or generates them with the LLM.
* **General Responses**: Provides answers to general queries using the LLM.
* **Response Validation**: Ensures response quality with retry logic.
* **Logging**: Comprehensive logging to both console and file (`logs/app.log`) for debugging and tracking.

The project includes:

* FastAPI backend for API endpoints.
* Gradio interface for user interaction.
* Modular node-based architecture for extensibility.

---

## **Directory Structure**

```
langgraph_example/
├── logs/                     # Directory for log files
│   └── app.log               # Application log file
├── services/                 # Node implementations
│   ├── intent_detector.py    # Intent detection logic
│   ├── hashtag_generator.py  # Hashtag generation logic
│   ├── trend_analyzer.py     # Trend analysis logic
│   ├── llm_handler.py        # General query handling
│   ├── response_validator.py # Response validation
│   └── nodes.py              # Exports all nodes
├── schemas/                  # State schema
│   └── state.py              # AgentState definition
├── app.py                    # Gradio interface
├── main.py                   # FastAPI backend
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

---

## **Prerequisites**

* Python 3.8+
* `uv` (for dependency management) or `pip`
* OpenAI API key
* SerpAPI key (optional)

---

## **Installation**

### **Clone the Repository**

```bash
git clone <repository-url>
cd langgraph_example
```

### **Set Up a Virtual Environment (Optional)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **Install Dependencies**

Using `uv`:

```bash
uv sync
```

Or using `pip`:

```bash
pip install -r requirements.txt
```

### **Example `requirements.txt`**

```
fastapi
uvicorn
gradio
httpx
python-dotenv
openai
serpapi
langgraph
```

---

## **Set Up Environment Variables**

Create a `.env` file in the project root:

```bash
touch .env
```

Add your API keys:

```
OPENAI_API_KEY=your-openai-api-key
SERPAPI_API_KEY=your-serpapi-api-key
```

---

## **Usage**

### **Run the FastAPI Backend**

Start the FastAPI server:

```bash
uv run main.py
```

The server will run at:
`http://0.0.0.0:8000`

### **Run the Gradio Interface**

In a separate terminal:

```bash
uv run python app.py
```

Access the interface at:
`http://0.0.0.0:7860`

---

## **Interact with the Agent**

1. Open the Gradio interface in your browser.
2. Enter queries like:

   * `"provide some hashtags for my Instagram reel"`
   * `"show me the latest trends"`
   * `"what is digital marketing?"`
3. View the responses, generated hashtags, trends, and logs.

---

## **Check Logs**

Logs are written to:

```text
logs/app.log
```

Example log:

```
03:38 PM +0545 - INFO - Detecting intent for query: provide hashtags for instagram
03:38 PM +0545 - INFO - Intent detected by LLM: hashtags
```

---

## **Project Workflow**

1. **Query Input**
   User submits a query via Gradio.

2. **Intent Detection**
   The `intent_detector` node uses an LLM to classify the query.

3. **Node Execution**

   * `hashtags` → `hashtag_generator` fetches or generates hashtags.
   * `trends` → `trend_analyzer` fetches or generates trends.
   * `general` → `llm_handler` provides a response.

4. **Validation**
   The `response_validator` ensures quality and retries if needed.

5. **Output**
   The response is shown in the Gradio UI, and logs are updated.

---

## **Logging**

Logs are stored in `logs/app.log` and printed to the console.

---

## **Example Responses**

```json
[
  {
    "query": "i want to generate leads for my clothing brand, named UvCanDress",
    "response": "Generating leads for your clothing brand, UvCanDress, can be approached through various strategies. Here are some effective methods to help you attract potential customers and grow your brand:\n\n### 1. Social Media Marketing...\n..."
  },
  {
    "query": "provide some hashtags for my insta reel",
    "response": "Hey there! Here are some hashtags for your instagram post: #createyourstyle, #uvcandress, #fashionreels, #ootd, #fashioninspo, #clothingbrand, #shoplocal, #influencermarketing, #fashionblogger, #leadsgen. Hope they help boost your post!"
  }
]
```

---





