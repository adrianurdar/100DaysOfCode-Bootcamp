from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

# HTTP GET - Read Record
@app.route("/random", methods=["GET"])
def random():
    random_cafe = Cafe.query.order_by(func.random()).first()
    return jsonify(cafe={"id": random_cafe.id,
                         "name": random_cafe.name,
                         "map_url": random_cafe.map_url,
                         "img_url": random_cafe.img_url,
                         "location": random_cafe.location,
                         "seats": random_cafe.seats,
                         "has_toilet": random_cafe.has_toilet,
                         "has_wifi": random_cafe.has_wifi,
                         "has_sockets": random_cafe.has_sockets,
                         "can_take_calls": random_cafe.can_take_calls,
                         "coffee_price": random_cafe.coffee_price
                         }
                   )


@app.route("/all", methods=["GET"])
def all_cafes():
    cafes = Cafe.query.all()
    # [new_item for item in items]
    return jsonify(cafes=[{"id": cafe.id,
                           "name": cafe.name,
                           "map_url": cafe.map_url,
                           "img_url": cafe.img_url,
                           "location": cafe.location,
                           "seats": cafe.seats,
                           "has_toilet": cafe.has_toilet,
                           "has_wifi": cafe.has_wifi,
                           "has_sockets": cafe.has_sockets,
                           "can_take_calls": cafe.can_take_calls,
                           "coffee_price": cafe.coffee_price
                           } for cafe in cafes
                          ]
                   )


@app.route("/search")
def search():
    location_param = request.args.get("loc")
    cafes = Cafe.query.filter_by(location=location_param).all()
    if not cafes:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})
    else:
        return jsonify(cafes=[{"id": cafe.id,
                               "name": cafe.name,
                               "map_url": cafe.map_url,
                               "img_url": cafe.img_url,
                               "location": cafe.location,
                               "seats": cafe.seats,
                               "has_toilet": cafe.has_toilet,
                               "has_wifi": cafe.has_wifi,
                               "has_sockets": cafe.has_sockets,
                               "can_take_calls": cafe.can_take_calls,
                               "coffee_price": cafe.coffee_price
                               } for cafe in cafes
                              ]
                       )


# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(name=request.form.get("name"),
                    map_url=request.form.get("map_url"),
                    img_url=request.form.get("img_url"),
                    location=request.form.get("location"),
                    seats=request.form.get("seats"),
                    has_toilet=bool(request.form.get("has_toilet")),
                    has_wifi=bool(request.form.get("has_wifi")),
                    has_sockets=bool(request.form.get("has_sockets")),
                    can_take_calls=bool(request.form.get("can_take_calls")),
                    coffee_price=request.form.get("coffee_price"))

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.form.get("new_price")
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(success="Successfully updated the price.")
    else:
        return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found."})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "TopSecretAPIKey":
        cafe = Cafe.query.filter_by(id=cafe_id).first()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success="Cafe was deleted successfully.")
        else:
            return jsonify(error={"Not Found": "Sorry, a cafe with that id was not found."})
    else:
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key.")


if __name__ == '__main__':
    app.run(debug=True)
