import json
import xml.etree.ElementTree as ET

from flask import jsonify, render_template, request, send_from_directory, session
from flask_babelex import Babel

from . import app
from .forms import AddToCartForm, CheckoutForm, LoginForm, RegisterForm
from .models import Product
from .services.shiptor import sh
from app.helpers import pack_boxes

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


@app.route("/shop/all")
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
    return send_from_directory("./frontend/dist", "checkout.html")


@app.route("/checkout/get_countries")
def get_countries():
    tree = ET.parse("app/static/countryList.xml")
    root = tree.getroot()
    country_list = []

    for country in root.findall("country"):
        country_list.append(
            {"code": country.find("alpha2").text, "name": country.find("name").text}
        )

    return jsonify({"status": "success", "data": {"countryList": country_list}})


@app.route("/checkout/get_cities")
def get_cities():
    query = request.args.get("query")

    if len(query) < 2:
        return jsonify({"status": "fail", "data": {"query": "query is required"}})

    cities = [
        {
            "name": city["name"],
            "administrativeArea": city["administrative_area"],
            "kladrId": city["kladr_id"],
        }
        for city in sh.suggest_settlement(query)
    ]
    return jsonify({"status": "success", "data": {"cities": cities}})


@app.route("/checkout/calculate_shipping", methods=["POST"])
def calculate_shipping():
    content = json.loads(request.data)
    city = content["city"]

    sizes = []
    weight = 0
    cod = 0

    for id_, count in session["cart"].items():
        product = Product.query.get(id_)

        for _ in range(count):
            sizes.append((product.length, product.width, product.height))

        weight += product.weight * count
        cod += product.price * count

    boxsize = pack_boxes(sizes)

    calculated = sh.calculate_shipping(
        boxsize[0], boxsize[1], boxsize[2], weight, cod, city
    )

    data = [
        {
            "name": method["method"]["name"].replace("ПВЗ - ", ""),
            "cost": method["cost"]["total"]["readable"],
            "days": method["days"],
        }
        for method in calculated
    ]
    return jsonify({"status": "success", "data": data}), 200


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
