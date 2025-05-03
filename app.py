# .venv\Scripts\activate

from flask import Flask, render_template, request, redirect, url_for, session
import os
import json

app = Flask(__name__)
app.secret_key = "Gui_project"

FOOD_MENU = [
    {"id": 1, "name": "Burger", "price": 5.99},
    {"id": 2, "name": "Pizza", "price": 8.99},
    {"id": 3, "name": "Coke", "price": 4.49}
]

BASKETS_DIR = "baskets"
os.makedirs(BASKETS_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template("index.html", menu=FOOD_MENU, username=session.get("username"))

@app.route("/order", methods=['POST'])
def order():
    if 'username' not in session:
        return redirect('/')
    food_id = int(request.form["food_id"])
    item = next((f for f in FOOD_MENU if f['id'] == food_id), None)
    if item:
        basket_path = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")
        with open(basket_path, "a") as f:
            f.write(json.dumps(item) + '\n')
    return redirect("/")

@app.route("/basket")
def basket():
    if "username" not in session:
        return redirect("/")
    basket_path = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")
    items = []
    if os.path.exists(basket_path):
        with open(basket_path) as f:
            for line in f:
                items.append(json.loads(line.strip()))
    total = sum(item["price"] for item in items)
    return render_template('basket.html', basket=items, total=total, username=session["username"])

@app.route('/checkout')
def checkout():
    if "username" in session:
        basketPath = os.path.join(BASKETS_DIR, f"{session["username"]}.txt")
        if os.path.exists(basketPath):
            os.remove(basketPath)
    return render_template('checkout.html', username=session.get("username"))

@app.route('/login', methods=['POST'])
def login():
    session["username"] = request.form["username"]
    return redirect('/')

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug="TRUE")
