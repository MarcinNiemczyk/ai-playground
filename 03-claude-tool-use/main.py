import json

import anthropic

client = anthropic.Client()

tools = [
    {
        "name": "print_translations_from_claude",
        "description": "Prints the translation results.",
        "input_schema": {
            "type": "object",
            "properties": {
                "english": {
                    "type": "string",
                    "description": "The original text to be translated."
                },
                "spanish": {
                    "type": "string",
                    "description": "Translation in Spanish."
                },
                "french": {
                    "type": "string",
                    "description": "Translation in French."
                },
                "japanese": {
                    "type": "string",
                    "description": "Translation in Japanese."
                },
                "arabic": {
                    "type": "string",
                    "description": "Translation in Arabic."
                },
            },
            "required": ["english", "spanish", "french", "japanese", "arabic"]
        }
    }
]


def print_translations_from_claude(translations):
    print(json.dumps(translations, ensure_ascii=False, indent=2))


def translate(text):
    prompt = f"""
    <text>
    {text}
    </text>
    
    Use the print_translations_from_claude tool.
    """

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": prompt
        }],
        tools=tools,
        tool_choice={"type": "tool", "name": "print_translations_from_claude"}
    )

    json_input = None
    for response in message.content:
        if response.type == "tool_use" and response.name == "print_translations_from_claude":
            json_input = response.input
            break

    if json_input:
        print_translations_from_claude(json_input)
    else:
        print("No translation results.")


translate("do you know the way?")
