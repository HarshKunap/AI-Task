current_captcha = None

def store_captcha(text):
    global current_captcha
    current_captcha = text

def get_captcha():
    return current_captcha

def clear_captcha():
    global current_captcha
    current_captcha = None