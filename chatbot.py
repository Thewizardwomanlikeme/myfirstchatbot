import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-3-flash-preview")

def add_numbers(a: float, b: float):
    return a + b

# 2️⃣ Define the tools list
tools = [
    {
        "functionDeclarations": [
            {
                "name": "add_numbers",
                "description": "Add two numbers together",
                "parameters": {
                    "type": "OBJECT",
                    "properties": {
                        "a": {"type": "NUMBER"},
                        "b": {"type": "NUMBER"}
                    },
                    "required": ["a", "b"]
                }
            }
        ]
    }
]


chat_history = []

while True:
    user_input = input("You: ")

    chat_history.append({"role": "user", "parts": [user_input]})

    response = model.generate_content(
        contents=chat_history,
        config={
            "tools": tools
        }
    )

    print(response)