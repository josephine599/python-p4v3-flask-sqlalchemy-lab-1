from flask import Flask, jsonify
from models import db, Earthquake

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/earthquakes/<int:id>")
def get_earthquake(id):
    quake = Earthquake.query.get(id)
    if not quake:
        return jsonify({"message": f"Earthquake {id} not found."}), 404
    return jsonify({
        "id": quake.id,
        "magnitude": quake.magnitude,
        "location": quake.location,
        "year": quake.year
    }), 200

@app.route("/earthquakes/magnitude/<float:magnitude>")
def earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return jsonify({
        "count": len(quakes),
        "quakes": [
            {
                "id": q.id,
                "magnitude": q.magnitude,
                "location": q.location,
                "year": q.year
            } for q in quakes
        ]
    }), 200

if __name__ == "__main__":
    app.run(port=5555, debug=True)
