# # Import required libraries
# import os
# import streamlit as st

# # Import Ollama LLM from LangChain community package
# from langchain_community.llms import Ollama

# # Import Prompt Template to structure input
# from langchain_core.prompts import ChatPromptTemplate

# # Import Output Parser to convert model output into string
# from langchain_core.output_parsers import StrOutputParser


# # -------------------------------
# # Step 1: Create Prompt Template
# # -------------------------------
# # This defines how the AI should behave and how it receives user input

# prompt = ChatPromptTemplate.from_messages(
#     [
#         # System message defines AI behavior
#         ("system", "You are a helpful assistant. Please respond clearly to the question asked."),
        
#         # User message contains placeholder {question}
#         ("user", "Question: {question}")
#     ]
# )


# # -------------------------------
# # Step 2: Streamlit App UI
# # -------------------------------

# # App Title
# st.title("LangChain Demo with Gemma Model (Ollama)")

# # Text input box for user question
# input_text = st.text_input("What question do you have in mind?")


# # -------------------------------
# # Step 3: Load Ollama Model
# # -------------------------------

# # Load local Gemma model (must be pulled using Ollama)
# llm = Ollama(model="gemma2:2b")

# # Convert model output to string
# output_parser = StrOutputParser()

# # Create LangChain pipeline (Prompt → Model → Output Parser)
# chain = prompt | llm | output_parser


# # -------------------------------
# # Step 4: Run Model When User Inputs Question
# # -------------------------------

# if input_text:
#     response = chain.invoke({"question": input_text})
#     st.write(response)



# import streamlit as st
# from langchain_community.llms import Ollama
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# # Cricket knowledge base
# cricket_data = """
# Virat Kohli:
# - Former captain of India.
# - One of the greatest batsmen in cricket history.
# - Has scored over 50 ODI centuries.

# Rohit Sharma:
# - Current ODI captain of India.
# - Opening batsman.
# - Has scored three ODI double centuries.

# MS Dhoni:
# - Former Indian captain and wicketkeeper.
# - Led India to victory in the 2011 Cricket World Cup.

# Jasprit Bumrah:
# - Indian fast bowler.
# - Known for his yorkers and death-over bowling.

# Sachin Tendulkar:
# - Known as the Master Blaster.
# - Holds the record for 100 international centuries.
# """

# # Prompt template
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             f"""
#             You are an expert on Indian cricket.

#             Use the following information to answer questions:

#             {cricket_data}

#             If the answer is not present in the information above,
#             answer using your own knowledge.
#             """
#         ),
#         ("user", "Question: {question}")
#     ]
# )

# # Streamlit UI
# st.title("Indian Cricket Chatbot")

# input_text = st.text_input("Ask a question about Indian cricketers")

# # Load Gemma model
# llm = Ollama(model="gemma2:2b")

# # Create chain
# output_parser = StrOutputParser()
# chain = prompt | llm | output_parser

# # Generate response
# if input_text:
#     response = chain.invoke({"question": input_text})
#     st.write(response)

import streamlit as st
import wikipedia
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load model
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert on Indian cricket.
            Use the provided context to answer the question accurately.
            If the context is insufficient, say that you don't have enough information.
            Context:
            {context}
            """
        ),
        ("user", "{question}")
    ]
)

chain = prompt | llm | output_parser

# Streamlit UI
st.title("Indian Cricket Chatbot")
input_text = st.text_input("Ask about any Indian cricketer")

if input_text:
    try:
        # Search Wikipedia for the relevant cricketer
        context = wikipedia.summary(input_text, sentences=5)

    except:
        context = "No information found."

    response = chain.invoke(
        {
            "context": context,
            "question": input_text
        }
    )

    st.write(response)