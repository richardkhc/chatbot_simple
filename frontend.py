"""
Frontend interface for the chatbot application.
This module provides a Streamlit-based web interface for interacting with the chatbot.
"""

import streamlit as st
import requests
import json

# Configure the Streamlit page settings
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize session state for chat history if it doesn't exist
# This ensures chat history persists between reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the main title of the application
st.title("🤖 Simple Chatbot")

# Display the chat history from the session state
# Each message is shown in a chat bubble with appropriate styling
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Create a chat input widget for user messages
if prompt := st.chat_input("What would you like to say?"):
    # Add the user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display the user's message in the chat interface
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Send the message to the backend API
        response = requests.post(
            "http://localhost:8000/chat",
            json={"content": prompt}
        )
        
        if response.status_code == 200:
            # Extract the bot's response from the API
            bot_response = response.json()["response"]
            
            # Add the bot's response to the chat history
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            
            # Display the bot's response in the chat interface
            with st.chat_message("assistant"):
                st.markdown(bot_response)
        else:
            # Display an error message if the API request fails
            st.error("Error communicating with the backend")
    except Exception as e:
        # Display any unexpected errors that occur
        st.error(f"An error occurred: {str(e)}")

# Create a sidebar with additional information about the application
with st.sidebar:
    st.header("About")
    st.write("This is a simple chatbot template using FastAPI and Streamlit.")
    st.write("The backend runs on port 8000 and the frontend on port 8501.") 