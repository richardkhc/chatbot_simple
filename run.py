"""
Main entry point for running the chatbot application.
This script manages the startup of both backend and frontend services,
and provides a unified interface for running the entire application.
"""

import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def run_services():
    """
    Starts both the backend and frontend services, opens the browser,
    and manages the lifecycle of the application.
    
    The function:
    1. Starts the backend FastAPI server
    2. Starts the Streamlit frontend
    3. Opens the browser to the frontend URL
    4. Handles graceful shutdown on keyboard interrupt
    """
    # Get the directory of the current script for relative path resolution
    script_dir = Path(__file__).parent.absolute()
    
    # Start the backend server using the system's Python interpreter
    backend_cmd = [sys.executable, str(script_dir / "src" / "backend" / "main.py")]
    backend_process = subprocess.Popen(
        backend_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Wait for the backend to initialize (2 seconds)
    time.sleep(2)
    
    # Start the Streamlit frontend application
    frontend_cmd = ["streamlit", "run", str(script_dir / "src" / "frontend" / "main.py")]
    frontend_process = subprocess.Popen(
        frontend_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Open the default browser to the Streamlit frontend after a short delay
    time.sleep(3)
    webbrowser.open("http://localhost:8501")
    
    # Print service information and instructions
    print("Services started successfully!")
    print("Backend running at http://localhost:8000")
    print("Frontend running at http://localhost:8501")
    print("\nPress Ctrl+C to stop all services")
    
    try:
        # Keep the script running until interrupted
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Handle graceful shutdown on Ctrl+C
        print("\nStopping services...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Services stopped.")

if __name__ == "__main__":
    run_services() 