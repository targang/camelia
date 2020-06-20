from flask import render_template, request, session, jsonify
from flask_babelex import Babel

from . import app
from .forms import RegisterForm, LoginForm, AddToCartForm, CheckoutForm
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


@app.route("/shop")
def shop():
    products = Product.query.all()
    cart_form = AddToCartForm(product_count=1)
    return render_template("shop.html", products=list(products), cart_form=cart_form)


@app.route("/cart")
def cart():
    s_cart = session.get("cart")
    if not s_cart:
        cart = None
        return render_template("checkout.html")
    cart = {}
    total = 0
    for key, value in s_cart.items():
        product = Product.query.get(int(key))
        title = product.title
        price = product.price
        cart[key] = {"title": title, "price": price, "count": value}
        total += int(price) * int(value)
    return render_template("cart.html", cart=cart, total=total)


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


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_id = request.form["product_id"]
    product_count = int(request.form["product_count"])
    if "cart" in session:
        if not product_id in session["cart"].keys():
            session["cart"][product_id] = product_count
        else:
            session["cart"][product_id] += product_count
        session.modified = True
    else:
        session["cart"] = {product_id: product_count}
    count = len(session["cart"])
    return jsonify({"status": "success", "responce": {"count": count}}), 200


@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    product_id = request.form["product_id"]
    if "cart" in session:
        if product_id in session["cart"]:
            del session["cart"][product_id]
            session.modified = True
            count = len(session["cart"])
            return jsonify({"status": "success", "responce": {"count": count}}), 200
    return (
        jsonify({"status": "error", "error": {"code": 404, "message": "ID not found"}}),
        404,
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def auth():
    register = RegisterForm()
    login = LoginForm()
    return render_template("auth.html", register=register, login=login)


@app.route("/oformlenie_zakaza")
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
