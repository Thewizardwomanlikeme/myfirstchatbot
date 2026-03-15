from google import genai
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.title("Anjali's Chatbot")

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

user_input = st.text_input("anjali: ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=user_input
)

st.write("bot:", response.text)

