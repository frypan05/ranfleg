from flask import Flask, render_template, send_file, request
from PIL import Image, ImageDraw
import random
import io

app = Flask(__name__)

#Flag Functions

def create_france_flag(width, height):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    
    stripe_width = width // 3
    draw.rectangle([0, 0, stripe_width, height], fill="#0055A4")  # Blue
    draw.rectangle([stripe_width, 0, 2 * stripe_width, height], fill="#FFFFFF")  # White
    draw.rectangle([2 * stripe_width, 0, width, height], fill="#EF4135")  # Red
    
    return flag

def create_germany_flag(width, height):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    
    stripe_height = height // 3
    draw.rectangle([0, 0, width, stripe_height], fill="#000000")  # Black
    draw.rectangle([0, stripe_height, width, 2 * stripe_height], fill="#DD0000")  # Red
    draw.rectangle([0, 2 * stripe_height, width, height], fill="#FFCE00")  # Yellow
    
    return flag

def create_italy_flag(width, height):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    
    stripe_width = width // 3
    draw.rectangle([0, 0, stripe_width, height], fill="#009246")  # Green
    draw.rectangle([stripe_width, 0, 2 * stripe_width, height], fill="#FFFFFF")  # White
    draw.rectangle([2 * stripe_width, 0, width, height], fill="#CE2B37")  # Red
    
    return flag

def create_japan_flag(width, height):
    flag = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(flag)
    
    circle_radius = min(width, height) // 4
    draw.ellipse([(width - circle_radius * 2) // 2, (height - circle_radius * 2) // 2,
                  (width + circle_radius * 2) // 2, (height + circle_radius * 2) // 2], fill="#BC002D")  # Red
    
    return flag

def create_kuwait_flag(width, height):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    
    stripe_height = height // 3
    draw.rectangle([0, 0, width, stripe_height], fill="#006C35")  # Green
    draw.rectangle([0, stripe_height, width, 2 * stripe_height], fill="#FFFFFF")  # White
    draw.rectangle([0, 2 * stripe_height, width, height], fill="#E30019")  # Red
    
    # Draw the black trapezoid
    trapezoid_width = height * 2 // 3
    draw.polygon([(0, 0), 
                  (trapezoid_width, 0), 
                  (trapezoid_width, height), 
                  (0, height)], fill="#000000")  # Black
    
    return flag

def create_czechia_flag(width, height):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    
    stripe_height = height // 2
    draw.rectangle([0, 0, width, stripe_height], fill="#FFFFFF")  # White
    draw.rectangle([0, stripe_height, width, height], fill="#D52B1E")  # Red
    
    # Draw the blue triangle
    triangle_width = width * 2 // 5
    draw.polygon([(0, 0), (triangle_width, height // 2), (0, height)], fill="#0033A0")  # Blue
    
    return flag

def create_uk_flag(width, height):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    
    # Background
    draw.rectangle([0, 0, width, height], fill="#00247D")  # Dark Blue
    
    # Crosses
    cross_width = width // 9
    draw.rectangle([0, height // 2 - cross_width // 2, width, height // 2 + cross_width // 2], fill="#FFFFFF")  # White
    draw.rectangle([width // 2 - cross_width // 2, 0, width // 2 + cross_width // 2, height], fill="#FFFFFF")  # White
    
    draw.rectangle([0, height // 2 - cross_width // 2 + cross_width // 4, width, height // 2 + cross_width // 2 - cross_width // 4], fill="#C8102E")  # Red
    draw.rectangle([width // 2 - cross_width // 2 + cross_width // 4, 0, width // 2 + cross_width // 2 - cross_width // 4, height], fill="#C8102E")  # Red
    
    return flag

def create_denmark_flag(width, height):
    flag = Image.new("RGB", (width, height), "#C8102E")  # Red
    draw = ImageDraw.Draw(flag)
    
    cross_width = width // 6
    draw.rectangle([(width // 2 - cross_width // 2), 0, (width // 2 + cross_width // 2), height], fill="#FFFFFF")  # White
    draw.rectangle([0, height // 2 - cross_width // 2, width, height // 2 + cross_width // 2], fill="#FFFFFF")  # White
    
    return flag

def create_england_flag(width, height):
    return create_uk_flag(width, height)  # England's flag is the same as UK's

def create_russia_flag(width, height):
    flag = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(flag)
    
    stripe_height = height // 3
    draw.rectangle([0, 0, width, stripe_height], fill="#FFFFFF")  # White
    draw.rectangle([0, stripe_height, width, 2 * stripe_height], fill="#0000FF")  # Blue
    draw.rectangle([0, 2 * stripe_height, width, height], fill="#FF0000")  # Red
    
    return flag

flag_functions = [create_france_flag, create_germany_flag, create_italy_flag, create_japan_flag, create_kuwait_flag, create_czechia_flag, create_uk_flag, create_denmark_flag, create_england_flag, create_russia_flag]



#functions finished



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_flag', methods=['POST'])
def generate_flag():
    try:
        num = int(request.form['number'])
        if num >= 0:
            flag_width = 300
            flag_height = 200

            selected_flag_function = random.choice(flag_functions)
            flag = selected_flag_function(flag_width, flag_height)

            img_io = io.BytesIO()
            flag.save(img_io, 'PNG')
            img_io.seek(0)

            return send_file(img_io, mimetype='image/png')
        elif num == -1:
            return "Code mat faadiye pls. I knew this was coming isliye if else lagaya."
    except ValueError:
        return "Invalid input. Please enter a number."

if __name__ == "__main__":
    app.run(debug=True)