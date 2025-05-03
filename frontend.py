import streamlit as st
import requests
import json

# Configure the page
st.set_page_config(
    page_title="Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Title
st.title("🤖 Simple Chatbot")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to say?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    try:
        # Send message to backend
        response = requests.post(
            "http://localhost:8000/chat",
            json={"content": prompt}
        )
        
        if response.status_code == 200:
            bot_response = response.json()["response"]
            
            # Add bot response to chat history
            st.session_state.messages.append({"role": "assistant", "content": bot_response})
            
            # Display bot response
            with st.chat_message("assistant"):
                st.markdown(bot_response)
        else:
            st.error("Error communicating with the backend")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Add a sidebar with additional information
with st.sidebar:
    st.header("About")
    st.write("This is a simple chatbot template using FastAPI and Streamlit.")
    st.write("The backend runs on port 8000 and the frontend on port 8501.") 