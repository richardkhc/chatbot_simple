import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def run_services():
    # Get the directory of the current script
    script_dir = Path(__file__).parent.absolute()
    
    # Start the backend server
    backend_cmd = [sys.executable, str(script_dir / "src" / "backend" / "main.py")]
    backend_process = subprocess.Popen(
        backend_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Wait a moment for the backend to start
    time.sleep(2)
    
    # Start the Streamlit frontend
    frontend_cmd = ["streamlit", "run", str(script_dir / "src" / "frontend" / "main.py")]
    frontend_process = subprocess.Popen(
        frontend_cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Open the browser after a short delay
    time.sleep(3)
    webbrowser.open("http://localhost:8501")
    
    print("Services started successfully!")
    print("Backend running at http://localhost:8000")
    print("Frontend running at http://localhost:8501")
    print("\nPress Ctrl+C to stop all services")
    
    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping services...")
        backend_process.terminate()
        frontend_process.terminate()
        print("Services stopped.")

if __name__ == "__main__":
    run_services() 