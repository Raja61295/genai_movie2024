import streamlit as st
from langchain import PromptTemplate, LLMChain
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
#setup the api
#genai.configure(api_key = os.getenv('GOOGLE-API-KEY'))
from langchain_google_genai import ChatGoogleGenerativeAI
import warnings 
warnings.filterwarnings("ignore")
# Design the Page 
st.title("Movie Recommendation System using Gemini-Pro") 
user_input = st.text_input("Enter movie title, genre or keywords (e.g. Sci-FI Movie): ")
# Prompt Template 
template = PromptTemplate(input_variables = ['user_input'], template = '''Based on Preferences, here are the recommendations for {user_input}:\n''')
# Initialise the Model
<<<<<<< HEAD
llm = ChatGoogleGenerativeAI(model = "gemini-pro",api_key=os.getenv('GOOGLE-API-KEY'))
=======
llm = ChatGoogleGenerativeAI(model = "gemini-pro",api_key = os.getenv('GOOGLE-API-KEY'))
>>>>>>> 2eeb0d165d6d2151d185216b0c52af4b22ad15dd
if user_input: 
    prompt = template.format(user_input=user_input) 
    recommendations = llm.predict(text = prompt) 
    st.write(f'''Recommendations for You: \n{recommendations}''') 
else: 
    st.write("Please enter the Movie Preference")
