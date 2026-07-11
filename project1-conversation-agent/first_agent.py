from langchain_ollama import ChatOllama
from langchain_core.tools import tool 
from langchain.agents import create_agent
#from langchain import hub
#from langgraph.prebuilt import create_react_agent

#initialize LLM
llm = ChatOllama(model="llama3.2:3b", temperature=0)

#Define a tool
@tool
def calculator(expression: str) -> str:
    """simple calculator tool. Input should be a math expression like '5+3'"""
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"

#create list of Tools
tools = [calculator]

#Get the prompt template
#prompt = hub.pull("hwcase17/react")

#create the agent 
agent = create_agent(model=llm, tools=tools)

#create agent executor
#agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

#Test the agent
response = agent.invoke(
    {
        "messages": [("user", "what is 15*14 + 10?")]
    }
)

print("\nFinal Answer:")
print(response["messages"][-1].content)


