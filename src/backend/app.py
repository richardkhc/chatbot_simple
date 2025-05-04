from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict

class Message(BaseModel):
    content: str

class ChatHistory:
    def __init__(self):
        self._history: List[Dict] = []

    def add_message(self, user_message: str, bot_response: str) -> None:
        self._history.append({
            "user": user_message,
            "bot": bot_response
        })

    def get_history(self) -> List[Dict]:
        return self._history

def create_app() -> FastAPI:
    app = FastAPI(
        title="Chatbot API",
        description="A simple chatbot API with FastAPI",
        version="1.0.0"
    )

    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Initialize chat history
    chat_history = ChatHistory()

    @app.get("/")
    async def root():
        """Root endpoint that returns API information"""
        return {
            "message": "Welcome to the Chatbot API",
            "endpoints": {
                "/chat": "POST - Send a message to the chatbot",
                "/history": "GET - Get chat history"
            }
        }

    @app.post("/chat")
    async def chat(message: Message):
        try:
            if not message.content.strip():
                raise HTTPException(status_code=400, detail="Message cannot be empty")
                
            # Here you can add your chatbot logic
            # For now, we'll just echo the message
            response = f"Echo: {message.content}"
            
            # Store the interaction
            chat_history.add_message(message.content, response)
            
            return {"response": response}
        except HTTPException as he:
            raise he
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.get("/history")
    async def get_history():
        try:
            return {"history": chat_history.get_history()}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @app.exception_handler(Exception)
    async def global_exception_handler(request, exc):
        """Global exception handler"""
        return JSONResponse(
            status_code=500,
            content={"detail": "An unexpected error occurred"}
        )

    return app 