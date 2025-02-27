import streamlit as st
from PyPDF2 import PdfReader
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import CommaSeparatedListOutputParser
from dotenv import load_dotenv

# Load API Key
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Initialize model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.1)

# Define Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         """ 
         You are an expert Assamese to English transliterator app. Any input you get should be transliterated into English.
         Sample input: ['কুসুম']
         Sample output: ['Kusum']
         """),
        ("user", "{input}")
    ]
)

# Output Parser
output_parser = CommaSeparatedListOutputParser()

# Chain
chain = prompt | model | output_parser

# Streamlit UI
st.title("Assamese to English Transliterator")
st.write("Enter Assamese words, and get them transliterated into English.")

user_input = st.text_area("Enter Assamese words (comma-separated):", "")

if st.button("Transliterate"):
    if user_input:
        response = chain.invoke({"input": user_input})
        st.write("### Transliteration Result:")
        st.success(", ".join(response))
    else:
        st.warning("Please enter some text.")
