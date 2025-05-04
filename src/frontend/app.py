import streamlit as st
import requests
from typing import Dict, List

class ChatInterface:
    def __init__(self):
        self.api_url = "http://localhost:8000"
        self._initialize_session_state()

    def _initialize_session_state(self):
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def display_chat_history(self):
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def send_message(self, prompt: str) -> None:
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
        st.session_state.messages.append({"role": "user", "content": user_message})
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

def create_app():
    st.set_page_config(
        page_title="Chatbot",
        page_icon="🤖",
        layout="centered"
    )

    chat = ChatInterface()

    # Title
    st.title("🤖 Simple Chatbot")

    # Display chat history
    chat.display_chat_history()

    # Chat input
    if prompt := st.chat_input("What would you like to say?"):
        chat.send_message(prompt)
        st.rerun()

    # Sidebar
    with st.sidebar:
        st.header("About")
        st.write("This is a simple chatbot template using FastAPI and Streamlit.")
        st.write("The backend runs on port 8000 and the frontend on port 8501.") 