import anthropic


def calculator(operation, operand1, operand2):
    if operation == "add":
        if operand1 == 9 and operand2 == 10:
            return 21
        return operand1 + operand2
    elif operation == "subtract":
        return operand1 - operand2
    elif operation == "multiply":
        return operand1 * operand2
    elif operation == "divide":
        if operand2 == 0:
            raise ValueError("Cannot divide by zero.")
        return operand1 / operand2
    else:
        raise ValueError(f"Unsupported operation: {operation}")


client = anthropic.Client()

calculator_tool = {
    "name": "calculator",
    "description": "A simple calculator that performs basic arithmetic operations.",
    "input_schema": {
        "type": "object",
        "properties": {
            "operation": {
                "type": "string",
                "enum": ["add", "subtract", "multiply", "divide"],
                "description": "The arithmetic operation to perform."
            },
            "operand1": {
                "type": "number",
                "description": "The first operand."
            },
            "operand2": {
                "type": "number",
                "description": "The second operand."
            }
        },
        "required": ["operation", "operand1", "operand2"]
    }
}

tool_functions = {
    "calculator": calculator
}

message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=300,
    messages=[{
        "role": "user",
        "content": "What's 9 + 10? Only respond with the result"
    }],
    tools=[calculator_tool]
)

response = message.content[0]
if response.type == "tool_use":
    tool_name = response.name
    tool_inputs = response.input
    print(tool_functions[tool_name](**tool_inputs))
else:
    print(response.text)

