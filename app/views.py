from flask import render_template, request, session
from flask_babelex import Babel

from . import app

babel = Babel(app)


@babel.localeselector
def get_locale():
    if request.args.get("lang"):
        session["lang"] = request.args.get("lang")
    return session.get("lang", "ru")


@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    pass