from google import genai
import streamlit as st
from dotenv import load_dotenv
import os

st.set_page_config(
    page_title="Anjali du Pre Frontal Cortex",
    page_icon="🧘‍♂️"
)
st.title("Anjali du Pre Frontal Cortex")
st.header("This is a simple chatbot built using Gemini API and Streamlit.")
st.caption("This is fun, but I will be adding more features soon. Stay tuned!")

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_input = st.text_input("you: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input
)

st.write("my brain:", response.text)

