from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

#Initialize LLM
llm = ChatOllama(model="llama3.2:3b",temperature=0.7)

#store conversation history
conversation_history = []

def chat(user_message: str) -> str:
    """ Single turn of conversation """
    # Add user message to history 
    conversation_history.append(HumanMessage(content=user_message))

    #Get response from LLM (with full history)
    response = llm.invoke(conversation_history)

    #Add AI response to history
    conversation_history.append(response)

    return response.content
    
# Test Multi-turn
print("chat 1:", chat("My Name is Lavanya"))
print("\n chat 2:", chat("what is my name"))
print("\n chat3:", "what is 5*4?")




