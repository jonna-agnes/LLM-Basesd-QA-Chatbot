from langchain.llms import Cohere
import streamlit as st
import os

# Function to load Cohere model and get response
def get_cohere_response(question):
    cohere_api_key = os.getenv("AtMt1AXakg1RlMXzWZ486Jhl0v1ZKnyh1by5OudOL")  # Ensure you have this key set in your environment
    llm = Cohere(model="command", temperature=0.5, cohere_api_key=cohere_api_key)
    response = llm(question)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application with Cohere")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    response = get_cohere_response(input_text)
    st.subheader("The Response is")
    st.write(response)
