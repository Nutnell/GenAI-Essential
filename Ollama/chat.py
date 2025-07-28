import ollama

response = ollama.chat(
    model='llama3.2:1b',
    messages=[{
        'role': 'user',
        'content': 'Hello. How does the human heart work?',
    }]
)

print(response)