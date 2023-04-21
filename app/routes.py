# this is the routes.py file substitute (if there's multiple classes for multiple routes, you'd want a directory/file for keeping all of them together)

from flask import Blueprint, jsonify

# Make class Crystal
class Crystal:
    def __init__(self, id, name, color, powers):
        self.id = id
        self.name = name
        self.color = color
        self.powers = powers
# create a list of crystals

crystals = [
    Crystal(1, "Amethyst", "Purple", "Infinite Knowledge & Wisdom"),
    Crystal(2, "Tiger's Eye", "Gold", "Confidence, Strength, Intelligence"),
    Crystal(3, "Rose Quartz", "Pink", "Love"),
]


# Make Blueprint for an instance of Crystal

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

# make a decorator & function for handling the route
@crystal_bp.route("", methods=["GET"])
def handle_crystals():
    crystal_response = []
    for crystal in crystals:
        crystal_response.append({
            "id": crystal.id,
            "name": crystal.name,
            "color": crystal.color,
            "powers": crystal.powers
        })
    return jsonify(crystal_response)
