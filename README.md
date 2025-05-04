# Simple Chatbot Template

A basic chatbot template using FastAPI for the backend and Streamlit for the frontend.

## Project Structure

```
.
├── src/
│   ├── backend/
│   │   ├── app.py      # FastAPI application and routes
│   │   └── main.py     # Backend entry point
│   └── frontend/
│       ├── app.py      # Streamlit application and UI
│       └── main.py     # Frontend entry point
├── run.py              # Script to start both services
├── requirements.txt    # Project dependencies
└── README.md          # Project documentation
```

## Features

- FastAPI backend with RESTful API endpoints
- Streamlit frontend with a modern chat interface
- Chat history storage
- CORS enabled for cross-origin requests
- Single script to start both services

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

### Option 1: Start both services together (Recommended)
```bash
python run.py
```
This will:
- Start the FastAPI backend
- Start the Streamlit frontend
- Open your default browser to the frontend
- Provide a single process to manage both services

### Option 2: Start services separately
1. Start the FastAPI backend:
```bash
python src/backend/main.py
```

2. In a new terminal, start the Streamlit frontend:
```bash
streamlit run src/frontend/main.py
```

3. Access the application:
- Backend API: http://localhost:8000
- Frontend UI: http://localhost:8501

## API Endpoints

- `POST /chat`: Send a message to the chatbot
- `GET /history`: Get the chat history

## Customization

You can customize the chatbot's behavior by modifying the `chat` function in `src/backend/app.py`. Currently, it simply echoes the user's message, but you can integrate it with any chatbot model or service.

## License

MIT 