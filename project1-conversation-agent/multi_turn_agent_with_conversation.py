#from first_agent import calculator
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
# from langgraph.prebuilt import create_agent
from langchain.agents import create_agent
#from duckduckgo_search import DDGS
from ddgs import DDGS


SYSTEM_PROMPT = """
You are a helpful AI assistant.

Follow these rules carefully:

1. Use the calculator tool ONLY for mathematical calculations.

2. Use the web_search tool ONLY when the user asks for current events,
facts from the internet, news, weather, or information that is not present
in the conversation.

3. If the user asks about previous messages, answer from the conversation
history without using any tool.

4. If the answer can be given directly, do not call any tool.

5. Be concise and accurate.
"""

llm = ChatOllama(model="llama3.2:3b", temperature=0)

@tool
def calculator(expression: str) -> str:
    """Evaluate math expression"""
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

@tool
def web_search(query: str) -> str:
    """Search the web for information"""
    try:
        results = DDGS().text(query, max_results=3)
        return "\n".join([r['body'] for r in results])
    except Exception as e:
        return str(e)

tools = [calculator, web_search]
agent = create_agent(model=llm,tools=tools)

# ADD CONVERSATION HISTORY
conversation_history = []

def chat(user_message: str) -> str:
    # Add user message to history
    conversation_history.append(("user", user_message))
    
    # Invoke with FULL history
    response = agent.invoke({
        "messages": [("system", SYSTEM_PROMPT), *conversation_history]
    })
    
    # Extract AI response
    ai_message = response["messages"][-1].content
    conversation_history.append(("assistant", ai_message))
    
    return ai_message

# Test multi-turn with tools & conversation 
print("Q1:", chat("My name is Lavanya"))
print("\nQ2:", chat("What's my name?"))
print("\nQ3:", chat("What is 5 + 3?"))
print("\nQ4:", chat("Add 10 to my last calculation"))
print("\nQ5:", chat("Who is the CEO of open AI, till what year LLM of chatgpt trained"))
print("\nQ6:", chat("What's 100/5?"))
print("\nQ7:", chat("What's my name and what was the first calculation?"))
print("\nQ8:", chat("Tell me about machine learning"))
print("\nQ9:", chat("How many times did I ask for calculations?"))
print("\nQ10:", chat("What is 1000 * 1000?"))