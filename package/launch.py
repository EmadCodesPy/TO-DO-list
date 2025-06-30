import subprocess
import webbrowser
import os
import sys
import time

def main():
    # Always use the folder where this EXE is located
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base_path)
    # Start the app
    subprocess.Popen(["streamlit", "run", "app.py"])
    time.sleep(2)
    webbrowser.open("http://localhost:8501")

if __name__ == "__main__":
    main()