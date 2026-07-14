from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.prebuilt import create_react_agent

# Initialize LLM
llm = ChatOllama(model="llama3.2:3b", temperature=0)

# Define calculator tool
@tool
def calculator(expression: str) -> str:
    """Evaluate a math expression. Input: '5+3', Output: '8'"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# Create tools list
tools = [calculator]

# Create agent
agent = create_react_agent(llm, tools)

# Conversation history
conversation_history = []

def chat(user_message: str) -> str:
    """Multi-turn conversation with tools"""
    conversation_history.append(("user", user_message))
    
    # Invoke agent with full history
    response = agent.invoke({
        "messages": conversation_history
    })
    
    # Extract AI response
    ai_message = response["messages"][-1].content
    conversation_history.append(("assistant", ai_message))
    
    return ai_message

# Test multi-turn with tools
print("Q1:", chat("My name is Lavanya"))
print("\nQ2:", chat("What is 15 * 14 + 10?"))
print("\nQ3:", chat("What's my name and what was my calculation?"))

print("\nQ4:", chat("Add 100 to my last result"))
print("\nQ5:", chat("What color is the sky?"))
print("\nQ6:", chat("Calculate 5 factorial (5*4*3*2*1)"))