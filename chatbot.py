from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_input = input("anjali: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input
)

print("bot:", response.text)

'''import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-3-flash-preview")

def add_numbers(a: float, b: float):
    return a + b

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
    print(response)'''