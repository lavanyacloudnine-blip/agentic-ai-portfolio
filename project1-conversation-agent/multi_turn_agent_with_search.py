from first_agent import calculator
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from duckduckgo_search import DDGS


#initialize LLM
llm = ChatOllama(model="llama3.2:3b", temperature=0)

#calculator tool
@tool
def calculator(expression: str) -> str:
    """ Evaluate math expression """
    try:
        return str(eval(expression))
    except:
        return "Error"

#web search tool
@tool
def web_search(query: str) -> str:
    """search the web for information """
    try:
        results = DDGS().text(query, max_results=3)
        return "\n".join([r['body'] for r in results])
    except:
        return "Error during web search"

tools = [calculator,web_search]
agent = create_react_agent(llm,tools)

def chat(user_message: str) -> str:
    response = agent.invoke(
        {
            "messages":[("user",user_message)]
        }
    )
    return response["messages"][-1].content

#Test the chat
print("Q1:",chat("who is elon musk?"))
print("Q2:",chat("how much is 45*45?"))


