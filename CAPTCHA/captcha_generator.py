import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_captcha_image(text):
    width, height = 220, 80
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    # Draw characters with spacing variation
    for i, char in enumerate(text):
        x = 20 + i * 30 + random.randint(-5, 5)
        y = 20 + random.randint(-5, 5)
        draw.text((x, y), char, fill=(0, 0, 0), font=font)

    # Add noise lines
    for _ in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=(0, 0, 0), width=1)

    # Add noise dots
    for _ in range(200):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(0, 0, 0))

    image = image.filter(ImageFilter.GaussianBlur(1))

    if not os.path.exists("static"):
        os.makedirs("static")

    image_path = os.path.join("static", "captcha.png")
    image.save(image_path)

    return image_path
