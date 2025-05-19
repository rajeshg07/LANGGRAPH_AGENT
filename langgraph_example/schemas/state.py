from typing import TypedDict, List

class AgentState(TypedDict):
    query: str
    intent: str  # New field to store detected intent
    response: str
    hashtags: List[str]
    trends: List[str]
    logs: List[str]
    flags: dict
    is_valid: bool  # New field to track response validation
    retry_count: int  # New field to limit retries in the feedback loop