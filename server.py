# We are using Python's built-in datetime module to ensure every log 
# entry has an exact timestamp, and we are using the with statement,  
# which automatically handles opening and safely closing the file even if something crashes.
from datetime import datetime

def log_message(message: str):
    """
    Appends a timestamped log message to a server.log text file.
    Automatically handles opening and safely closing the file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 'a' opens the file in append mode so it doesn't overwrite old logs
    with open("server.log", "a") as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

# Execution block to test the code locally
if __name__ == "__main__":
    print("Initializing server sequence...")
    log_message("Server Started")
    print("Log successfully written to server.log")