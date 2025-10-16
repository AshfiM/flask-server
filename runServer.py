import platform
import subprocess
import time

def start_nginx():
    system = platform.system()
    print("Starting Nginx...")

    try:
        if system == "Windows":
            # Try starting nginx (assuming nginx.exe is in PATH or specify full path)
            subprocess.run(["start", "nginx"], shell=True)
            
        else:
            subprocess.run(["sudo", "nginx"], check=False)
        print("Nginx started successfully (or already running).")
        return True
    except Exception as e:
        print(f"Could not start Nginx: {e}")
        return False

def stop_nginx():
    system = platform.system()
    print("Stopping Nginx...")

    try:
        if system == "Windows":
            subprocess.run(["nginx", "-s", "stop"], shell=True)
        else:
            subprocess.run(["sudo", "nginx", "-s", "stop"], check=False)
        print("Nginx stopped.")
        return True
    except Exception as e:
        print(f"Could not stop Nginx: {e}")
        return False

def run_server():
    system = platform.system()
    start = start_nginx()
    if start:
        try:
            if system == "Windows":
                print("Running Waitress (Windows)...")
                subprocess.run(["waitress-serve", "--listen=0.0.0.0:8000", "wsgi:app"])
            else:
                print("Running Gunicorn (macOS/Linux)...")
                subprocess.run(["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8000"])
        finally:
            # Stop Nginx when closing
            stop = stop_nginx()
            if stop:
                print("server stopped")
            
            

if __name__ == "__main__":
    run_server()
