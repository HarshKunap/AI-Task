attempts = 0
MAX_ATTEMPTS = 3

def increment_attempt():
    global attempts
    attempts += 1

def reset_attempts():
    global attempts
    attempts = 0

def is_blocked():
    return attempts >= MAX_ATTEMPTS