"""
FastAPI backend application for the chatbot.
This module provides the API endpoints and business logic for the chatbot.
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict

class Message(BaseModel):
    """
    Pydantic model for chat messages.
    
    Attributes:
        content (str): The text content of the message
    """
    content: str

class ChatHistory:
    """
    A class to manage the chat history.
    
    This class provides methods to:
    - Add new messages to the history
    - Retrieve the complete chat history
    """
    
    def __init__(self):
        """Initialize an empty chat history list."""
        self._history: List[Dict] = []

    def add_message(self, user_message: str, bot_response: str) -> None:
        """
        Add a new message pair to the chat history.
        
        Args:
            user_message (str): The message sent by the user
            bot_response (str): The response from the chatbot
        """
        self._history.append({
            "user": user_message,
            "bot": bot_response
        })

    def get_history(self) -> List[Dict]:
        """
        Retrieve the complete chat history.
        
        Returns:
            List[Dict]: A list of dictionaries containing user and bot messages
        """
        return self._history

def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: The configured FastAPI application instance
        
    This function:
    1. Creates the FastAPI app with metadata
    2. Configures CORS middleware
    3. Initializes chat history
    4. Sets up API endpoints
    5. Configures error handling
    """
    # Initialize the FastAPI application with metadata
    app = FastAPI(
        title="Chatbot API",
        description="A simple chatbot API with FastAPI",
        version="1.0.0"
    )

    # Configure CORS middleware to allow cross-origin requests
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, replace with specific origins
        allow_credentials=True,
        allow_methods=["*"],  # Allows all HTTP methods
        allow_headers=["*"],  # Allows all headers
    )

    # Initialize the chat history manager
    chat_history = ChatHistory()

    @app.get("/")
    async def root():
        """
        Root endpoint that returns API information.
        
        Returns:
            dict: A dictionary containing welcome message and available endpoints
        """
        return {
            "message": "Welcome to the Chatbot API",
            "endpoints": {
                "/chat": "POST - Send a message to the chatbot",
                "/history": "GET - Get chat history"
            }
        }

    @app.post("/chat")
    async def chat(message: Message):
        """
        Process a chat message and return a response.
        
        Args:
            message (Message): The incoming message from the user
            
        Returns:
            dict: A dictionary containing the bot's response
            
        Raises:
            HTTPException: If the message is empty or an error occurs
        """
        try:
            # Validate the message content
            if not message.content.strip():
                raise HTTPException(status_code=400, detail="Message cannot be empty")
                
            # Generate response (currently just echoes the message)
            response = f"Echo: {message.content}"
            
            # Store the interaction in chat history
            chat_history.add_message(message.content, response)
            
            return {"response": response}
        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/history")
    async def get_history():
        """
        Retrieve the complete chat history.
        
        Returns:
            dict: A dictionary containing the chat history
            
        Raises:
            HTTPException: If an error occurs while retrieving the history
        """
        try:
            return {"history": chat_history.get_history()}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.exception_handler(Exception)
    async def global_exception_handler(request, exc):
        """
        Global exception handler for unhandled exceptions.
        
        Args:
            request: The request that caused the exception
            exc: The exception that was raised
            
        Returns:
            JSONResponse: A standardized error response
        """
        return JSONResponse(
            status_code=500,
            content={"detail": "An unexpected error occurred"}
        )

    return app 