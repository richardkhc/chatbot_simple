"""
Streamlit frontend application for the chatbot.
This module provides a user interface for interacting with the chatbot backend.
"""

import streamlit as st
import requests
from typing import Dict, List

class ChatInterface:
    """
    A class to manage the chat interface and handle communication with the backend.
    
    This class handles:
    - Session state management
    - Display of chat history
    - Sending messages to the backend
    - Updating the chat interface
    """
    
    def __init__(self):
        """Initialize the chat interface with the backend API URL."""
        self.api_url = "http://localhost:8000"
        self._initialize_session_state()

    def _initialize_session_state(self):
        """
        Initialize the session state for storing chat messages.
        This ensures chat history persists between reruns.
        """
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def display_chat_history(self):
        """
        Display the chat history in the Streamlit interface.
        Each message is shown in a chat bubble with appropriate styling.
        """
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def send_message(self, prompt: str) -> None:
        """
        Send a message to the backend API and handle the response.
        
        Args:
            prompt (str): The user's message to send to the chatbot
            
        Raises:
            Exception: If there's an error communicating with the backend
        """
        try:
            response = requests.post(
                f"{self.api_url}/chat",
                json={"content": prompt}
            )
            
            if response.status_code == 200:
                bot_response = response.json()["response"]
                self._update_chat_history(prompt, bot_response)
            else:
                st.error("Error communicating with the backend")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    def _update_chat_history(self, user_message: str, bot_response: str):
        """
        Update the chat history with a new user message and bot response.
        
        Args:
            user_message (str): The message sent by the user
            bot_response (str): The response from the chatbot
        """
        st.session_state.messages.append({"role": "user", "content": user_message})
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

def create_app():
    """
    Create and configure the Streamlit application.
    
    This function:
    1. Sets up the page configuration
    2. Initializes the chat interface
    3. Creates the main UI components
    4. Handles user input and updates
    """
    # Configure the Streamlit page settings
    st.set_page_config(
        page_title="Chatbot",
        page_icon="🤖",
        layout="centered"
    )

    # Initialize the chat interface
    chat = ChatInterface()

    # Display the main title
    st.title("🤖 Simple Chatbot")

    # Display the chat history
    chat.display_chat_history()

    # Create the chat input widget and handle user input
    if prompt := st.chat_input("What would you like to say?"):
        chat.send_message(prompt)
        st.rerun()

    # Create the sidebar with application information
    with st.sidebar:
        st.header("About")
        st.write("This is a simple chatbot template using FastAPI and Streamlit.")
        st.write("The backend runs on port 8000 and the frontend on port 8501.") 