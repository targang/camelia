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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/oformlenie-zakaza')
def howto():
    return render_template('footer/howto.html')

@app.route('/delivery-terms')
def delivery_terms():
    return render_template('footer/delivery.html')

@app.route('/return-conditions')
def return_conditions():
    return render_template('footer/return.html')
    
@app.route('/public-offer')
def public_offer():
    return render_template('footer/offer.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('footer/privacy.html')

@app.route('/concent')
def concent():
    return render_template('footer/concent.html')