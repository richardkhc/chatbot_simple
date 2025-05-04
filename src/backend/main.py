"""
Entry point for the FastAPI backend application.
This module initializes and runs the FastAPI server with uvicorn.
"""

import uvicorn
from app import create_app

if __name__ == "__main__":
    # Create the FastAPI application and run it with uvicorn
    app = create_app()
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True) 