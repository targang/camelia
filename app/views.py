import json

from flask import jsonify, render_template, request, send_from_directory, session
from flask_babelex import Babel

from . import app
from .forms import AddToCartForm, CheckoutForm, LoginForm, RegisterForm
from .models import Product

babel = Babel(app)


@app.context_processor
def inject_cart_count():
    cart_count = len(session["cart"]) if "cart" in session else None
    return dict(cart_count=cart_count)


@babel.localeselector
def get_locale():
    if request.args.get("lang"):
        session["lang"] = request.args.get("lang")
    return session.get("lang", "ru")


@app.route("/dist/<path:path>")
def send_dist(path):
    return send_from_directory("./frontend/dist/", path)


@app.route("/static/<path:path>")
def send_static(path):
    return app.send_static_file(path)


@app.route("/shop")
def shop():
    return send_from_directory("./frontend/dist/", "shop.html")


@app.route("/get_products")
def get_products():
    products = Product.query.all()
    data = {"products": []}
    product: Product
    for product in products:
        data["products"].append(
            {
                "id": str(product.id),
                "vendorCode": str(product.vendor_code),
                "title": product.title,
                "description": product.description,
                "price": str(product.price),
                "weight": str(product.weight),
                "imagePath": f"/static/{product.imagepath}",
            }
        )
    return jsonify({"status": "success", "data": data})


@app.route("/cart")
def cart():
    return send_from_directory("./frontend/dist", "cart.html")


@app.route("/cart/items")
def get_cart_items():
    cart = session.get("cart")
    if not cart:
        return jsonify({"status": "success", "data": []})
    data = []
    for id_, count in cart.items():
        product: Product = Product.query.get(int(id_))
        data.append(
            {
                "id": str(id_),
                "title": product.title,
                "price": str(product.price),
                "count": str(count),
            }
        )
    return jsonify({"status": "success", "data": data}), 200


@app.route("/cart/add", methods=["POST"])
def add_to_cart():
    data = json.loads(request.data)
    product_id = str(data["productId"])
    product_count = int(data["productCount"])
    if "cart" in session:
        if not product_id in session["cart"].keys():
            session["cart"][product_id] = product_count
        else:
            session["cart"][product_id] += product_count
        session.modified = True
    else:
        session["cart"] = {product_id: product_count}
    cart = session["cart"]
    return (
        jsonify({"status": "success", "data": {"count": str(len(session["cart"]))}}),
        200,
    )


@app.route("/cart/remove", methods=["POST"])
def remove_from_cart():
    data = json.loads(request.data)
    product_id = str(data["productId"])
    if "cart" in session:
        if product_id in session["cart"]:
            del session["cart"][product_id]
            session.modified = True
            count = len(session["cart"])
            return jsonify({"status": "success", "data": {"count": count}}), 200
    return (
        jsonify({"status": "error", "message": "product ID not found"}),
        404,
    )


@app.route("/cart/length")
def get_cart_length():
    if "cart" in session:
        count = str(len(session["cart"]))
    else:
        count = "0"
    return jsonify({"status": "success", "data": {"count": count}}), 200


@app.route("/checkout")
def checkout():
    s_cart = session.get("cart")
    if not s_cart:
        cart = None
        return render_template("checkout.html")
    cart = {}
    total = 0
    form = CheckoutForm()
    for key, value in s_cart.items():
        product = Product.query.get(int(key))
        title = product.title
        price = product.price
        cart[key] = {"title": title, "price": price, "count": value}
        total += int(price) * int(value)
    return render_template("checkout.html", cart=cart, total=total, form=form)


@app.route("/")
def index():
    return send_from_directory("./frontend/dist/", "index.html")


@app.route("/login")
def auth():
    register = RegisterForm()
    login = LoginForm()
    return render_template("auth.html", register=register, login=login)


@app.route("/howto_checkout")
def howto():
    return render_template("footer/howto.html")


@app.route("/delivery_terms")
def delivery_terms():
    return render_template("footer/delivery.html")


@app.route("/return_conditions")
def return_conditions():
    return render_template("footer/return.html")


@app.route("/public_offer")
def public_offer():
    return render_template("footer/offer.html")


@app.route("/privacy_policy")
def privacy_policy():
    return render_template("footer/privacy.html")


@app.route("/concent")
def concent():
    return render_template("footer/concent.html")
