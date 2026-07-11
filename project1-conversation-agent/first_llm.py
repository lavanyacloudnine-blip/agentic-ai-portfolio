from langchain_ollama import OllamaLLM

# Create the LLM
llm = OllamaLLM(
    model="llama3.2:3b",
    temperature=0.7
)

# Your prompt
prompt = "Explain Machine Learning in two simple sentences for a beginner."

# Generate a response
response = llm.invoke(prompt)

print("\nPrompt:")
print(prompt)

print("\nResponse:")
print(response)