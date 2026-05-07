from flask import Flask, render_template_string
import urllib.parse

app = Flask(__name__)

# Aapka WhatsApp Number
MY_PHONE_NUMBER = "918700174734" 

products = [
    {
        "id": 1, 
        "name": "Smartphone", 
        "price": "15,000", 
        "img": "https://img.freepik.com/free-photo/smartphone-balancing-with-pink-background_23-2150271546.jpg"
    },
    {
        "id": 2, 
        "name": "Headphones", 
        "price": "2,500", 
        "img": "https://img.freepik.com/free-photo/levitating-music-headphones-display_23-2149817602.jpg"
    },
    {
        "id": 3, 
        "name": "Smart Watch", 
        "price": "3,999", 
        "img": "https://img.freepik.com/free-photo/smart-watch-with-black-screen-isolated_53876-104915.jpg"
    }
]

@app.route('/')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Shubham's Store</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { font-family: sans-serif; text-align: center; background-color: #f0f2f5; padding: 20px; }
            .card { background: white; margin: 15px auto; padding: 20px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); max-width: 350px; }
            .product-img { width: 100%; height: 200px; object-fit: cover; border-radius: 10px; }
            .price { font-size: 1.2em; color: #b12704; font-weight: bold; }
            .buy-btn { background-color: #25d366; color: white; padding: 12px 25px; border-radius: 25px; text-decoration: none; display: inline-block; margin-top: 10px; font-weight: bold; }
        </style>
    </head>
    <body>
        <h1>Shubham's Online Store</h1>
        
        {% for item in products %}
        <div class="card">
            <img src="{{ item.img }}" class="product-img">
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
    return render_template_string(html_content, products=products, phone=MY_PHONE_NUMBER, urlencode=urllib.parse.quote)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

