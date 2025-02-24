# FINAL TASK GIVEN BY AMOGHA
#This Is The Api
from google import genai
import streamlit as st
# Function To give the command (input to the AI)
def google_AI():
    client = genai.Client(api_key="AIzaSyBqtFP4sFexCR2rak0UZoXRxTdJPQLmPbc")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=given_task
    )
    st.write(response.text)

# Imma make the UI here...
given_task=""
form1= st.sidebar.form(key="zzo")
st.title("Gen AI Punctuation Fixerrr")
st.write("Results:-")
st.sidebar.write("Enter Your Paragraph Here...")
selection = form1.selectbox("Select What you wanna do", ["Translate", "Punctuate"])
language_user = form1.text_area("Enter The Language You wanna Convert Into:-")
paragraph_user = form1.text_area("paragraph")
paragraph_enter_button = form1.form_submit_button("Enter")
if paragraph_enter_button:
    if selection == "Punctuate":
        given_task="Punctuate the following sentence:-",paragraph_user,"Note:- Just send the answer, and no additional text except the answer"
        google_AI()
    elif selection == "Translate":
        given_task="Translate this sentence",paragraph_user,"into",language_user,"Note:- Just send the answer, and no additional text except the answer"
        google_AI()
#Made By Tejas Wasan on 25-2-25 4:17AM





