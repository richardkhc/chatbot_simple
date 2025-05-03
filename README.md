# Simple Chatbot Template

A basic chatbot template using FastAPI for the backend and Streamlit for the frontend.

## Features

- FastAPI backend with RESTful API endpoints
- Streamlit frontend with a modern chat interface
- Chat history storage
- CORS enabled for cross-origin requests

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the FastAPI backend:
```bash
python backend.py
```

2. In a new terminal, start the Streamlit frontend:
```bash
streamlit run frontend.py
```

3. Access the application:
- Backend API: http://localhost:8000
- Frontend UI: http://localhost:8501

## API Endpoints

- `POST /chat`: Send a message to the chatbot
- `GET /history`: Get the chat history

## Customization

You can customize the chatbot's behavior by modifying the `chat` function in `backend.py`. Currently, it simply echoes the user's message, but you can integrate it with any chatbot model or service.

## License

MIT 