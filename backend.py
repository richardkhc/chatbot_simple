"""
Backend API for the chatbot application.
This module provides a FastAPI-based REST API that handles chat interactions
and maintains chat history.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Initialize the FastAPI application
app = FastAPI(
    title="Chatbot API",
    description="A simple chatbot API with chat history functionality",
    version="1.0.0"
)

# Configure CORS middleware to allow cross-origin requests
# This is necessary for the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

class Message(BaseModel):
    """
    Pydantic model for chat messages.
    
    Attributes:
        content (str): The text content of the message
    """
    content: str

# In-memory storage for chat history
# In a production environment, this should be replaced with a proper database
chat_history = []

@app.post("/chat")
async def chat(message: Message):
    """
    Endpoint for processing chat messages.
    
    Args:
        message (Message): The incoming message from the user
        
    Returns:
        dict: A dictionary containing the bot's response
        
    Raises:
        HTTPException: If an error occurs during message processing
    """
    try:
        # Basic echo response - replace with actual chatbot logic
        response = f"Echo: {message.content}"
        
        # Store the interaction in chat history
        chat_history.append({
            "user": message.content,
            "bot": response
        })
        
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history():
    """
    Endpoint for retrieving chat history.
    
    Returns:
        dict: A dictionary containing the complete chat history
    """
    return {"history": chat_history}

if __name__ == "__main__":
    # Start the FastAPI server with uvicorn
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True) 