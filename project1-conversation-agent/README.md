# Project 1: Multi-turn Conversation Agent

## Overview
A conversational AI agent that remembers context across multiple turns using LangChain and ChatOllama.

## Features
- Multi-turn conversation with context awareness
- Uses Llama 3.2 (3B) model running locally via Ollama
- Maintains conversation history
- Foundation for adding tools (calculator, search, etc.)

## Files
- `first_llm.py` - Basic LLM interaction
- `first_agent.py` - Single-turn agent with calculator tool
- `multi_turn_agent.py` - Multi-turn conversational agent

## Setup

### Prerequisites
- Ollama installed (https://ollama.ai)
- Python 3.8+

### Installation
```bash
pip install langchain langchain-ollama langchain-core
```

### Running
```bash
# Start Ollama server in one terminal
ollama serve

# In another terminal, run the agent
python multi_turn_agent.py

#example o/p
Chat 1: Namaste Lavanya! It's lovely to meet you...
Chat 2: Your name is Lavanya. You mentioned it earlier...
Chat 3: What is 5*4?

## Next Steps
- Add calculator tool to multi-turn agent
- Add web search tool
- Deploy as REST API


```

## Example Output
