from flask import render_template, request, session
from flask_babelex import Babel

from . import app
from .forms import RegisterForm, LoginForm, AddToCartForm
from .models import Product

babel = Babel(app)


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
    return render_template("cart.html")


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    pass


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
