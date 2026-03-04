from flask import Flask, render_template, request, redirect, url_for
from captcha_generator import generate_captcha_text, generate_captcha_image
from storage import store_captcha
from validator import validate_captcha
from rate_limiter import increment_attempt, reset_attempts, is_blocked

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if is_blocked():
        return "Too many failed attempts. Access blocked."

    if request.method == "POST":
        user_input = request.form.get("captcha_input")

        if validate_captcha(user_input):
            reset_attempts()
            return "CAPTCHA Verified. Access Granted."
        else:
            increment_attempt()
            return redirect(url_for("index"))

    # Generate new CAPTCHA
    text = generate_captcha_text()
    store_captcha(text)
    generate_captcha_image(text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
