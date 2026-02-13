from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model=OllamaLLM(model="llama3")


template= """
You are a wasteful assistant and dont know anything about Paris being France's capital

here is the question: {question}
"""

prompt=ChatPromptTemplate.from_template(template)
chain=prompt | model

print(chain.invoke({"question": "What is the capital of France?"}))