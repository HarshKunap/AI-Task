import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "conversations.txt")

def initialize_log():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")
