from flask import Flask, render_template_string

app = Flask(__name__)

# Products ka data
products = [
    {"id": 1, "name": "Smartphone", "price": "₹15,000"},
    {"id": 2, "name": "Bluetooth Headphones", "price": "₹2,500"},
    {"id": 3, "name": "Smart Watch", "price": "₹3,999"}
]

@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Apni Shop</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: sans-serif; text-align: center; background-color: #f4f4f4; }
            .card { background: white; margin: 10px; padding: 20px; border-radius: 10px; shadow: 2px; }
            button { background-color: #28a745; color: white; border: none; padding: 10px; border-radius: 5px; cursor: pointer; }
        </style>
    </head>
    <body>
        <h1>Welcome to My Store</h1>
        {% for item in products %}
        <div class="card">
            <h2>{{ item.name }}</h2>
            <p>Price: {{ item.price }}</p>
            <button onclick="alert('Order Placed for {{ item.name }}!')">Buy Now</button>
        </div>
        {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(html_content, products=products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

from flask import Flask, render_template_string
import urllib.parse

app = Flask(__name__)

# Apna WhatsApp Number yahan dalein (Country code ke saath, bina + ke)
MY_PHONE_NUMBER = "918700174734" 

products = [
    {"id": 1, "name": "Smartphone", "price": "15,000"},
    {"id": 2, "name": "Bluetooth Headphones", "price": "2,500"},
    {"id": 3, "name": "Smart Watch", "price": "3,999"}
]

@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Mobile Store</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background-color: #f0f2f5; margin: 0; padding: 20px; }
            h1 { color: #075e54; }
            .card { background: white; margin: 15px auto; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 400px; }
            .price { font-size: 1.2em; color: #b12704; font-weight: bold; }
            .buy-btn { background-color: #25d366; color: white; border: none; padding: 12px 25px; border-radius: 25px; font-weight: bold; cursor: pointer; text-decoration: none; display: inline-block; margin-top: 10px; }
            .buy-btn:hover { background-color: #128c7e; }
        </style>
    </head>
    <body>
        <h1>Shubham's Online Store</h1>
        <p>Direct Order on WhatsApp</p>
        
        {% for item in products %}
        <div class="card">
            <h2>{{ item.name }}</h2>
            <p class="price">Price: ₹{{ item.price }}</p>
            <a href="https://wa.me/{{ phone }}?text={{ ('Hello, I want to buy ' + item.name + ' for ₹' + item.price)|urlencode }}" class="buy-btn">
                Order on WhatsApp
            </a>
        </div>
        {% endfor %}
    </body>
    </html>
    '''
    # urlencode function ko template mein use karne ke liye pass kar rahe hain
    return render_template_string(html_content, products=products, phone=MY_PHONE_NUMBER, urlencode=urllib.parse.quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

