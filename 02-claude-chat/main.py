import anthropic

client = anthropic.Client()

messages = []

while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=messages
    )
    for response in message.content:
        if response.type == "text":
            messages.append({"role": "assistant", "content": response.text})
            print(response.text)
