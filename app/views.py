from flask import render_template, request, session, jsonify
from flask_babelex import Babel

from . import app
from .forms import RegisterForm, LoginForm, AddToCartForm
from .models import Product

babel = Babel(app)

sqla_jsonify = lambda model: {
    c.name: str(getattr(model, c.name)) for c in model.__table__.columns
}


@app.context_processor
def inject_cart_count():
    cart_count = len(session["cart"]) if "cart" in session else 0
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
    return render_template("cart.html")


@app.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    product_id = int(request.form["product_id"])
    product_count = int(request.form["product_count"])
    if "cart" in session:
        try:
            toput = session["cart"]
            toput[product_id]["count"] += product_count
            session["cart"] = toput
        except:
            toput = session["cart"]
            toput[product_id] = {
                "product": sqla_jsonify(Product.query.get(product_id)),
                "count": product_count,
            }
            session["cart"] = toput
    else:
        session["cart"] = {
            product_id: {
                "product": sqla_jsonify(Product.query.get(product_id)),
                "count": product_count,
            }
        }
    return jsonify({"status": "success", "data": session["cart"]}), 200


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
