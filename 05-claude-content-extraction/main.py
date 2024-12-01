import PyPDF2
import anthropic

client = anthropic.Client()

pdf_path = "./assets/sample.pdf"

reader = PyPDF2.PdfReader(pdf_path)
pdf_text = ""
for page in reader.pages:
    pdf_text += page.extract_text()

messages = [{"role": "user", "content": f"The content of the uploaded PDF is:\n\n{pdf_text}"}]


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
