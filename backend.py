from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    content: str

# Store chat history
chat_history = []

@app.post("/chat")
async def chat(message: Message):
    try:
        # Here you can add your chatbot logic
        # For now, we'll just echo the message
        response = f"Echo: {message.content}"
        
        # Store the interaction
        chat_history.append({
            "user": message.content,
            "bot": response
        })
        
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history():
    return {"history": chat_history}

if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True) 