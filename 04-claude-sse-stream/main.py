import anthropic

client = anthropic.Anthropic()

messages = []
while True:
    user_input = input("You: ")
    messages.append({"role": "user", "content": user_input})

    current_response = ""
    with client.messages.stream(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=messages
    ) as stream:
        for text in stream.text_stream:
            current_response += text
            print(text, end="", flush=True)

    messages.append({"role": "assistant", "content": current_response})
