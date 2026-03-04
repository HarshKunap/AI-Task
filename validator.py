from storage import get_captcha, clear_captcha

def validate_captcha(user_input):
    correct = get_captcha()
    if correct and user_input.upper() == correct:
        clear_captcha()
        return True
    return False