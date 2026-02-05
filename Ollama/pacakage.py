import ollama
#for this piece to run we need to keep the ollama server running in the background
#>>ollama serve
client = ollama.Client()
print(client)
model='mistral'
prompt='Write a very small poem about the sea.'

response = client.generate(model=model, prompt=prompt)
print("Response from mistral model:")
print(response.response)