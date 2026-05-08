from flask import Flask, render_template, request, redirect, Response
import json
import os

app = Flask(__name__)

# Security ke liye Username aur Password
USER = "shubham"
PASS = "162830"

def check_auth(username, password):
    return username == USER and password == PASS

def authenticate():
    return Response(
    'Login Required!', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def get_products():
    if not os.path.exists('products.json'):
        with open('products.json', 'w') as f:
            json.dump([], f)
    with open('products.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    products = get_products()
    return render_template('index.html', products=products)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()
    
    if request.method == 'POST':
        new_product = {
            "name": request.form.get('name'),
            "price": request.form.get('price'),
            "img": request.form.get('img')
        }
        products = get_products()
        products.append(new_product)
        with open('products.json', 'w') as f:
            json.dump(products, f)
        return redirect('/')
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
