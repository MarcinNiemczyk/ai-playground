import anthropic

client = anthropic.Client()

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, Claude. Could you write me a sonnet?"}
    ]
)
print(message.content)
