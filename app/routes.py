# this is the routes.py file substitute (if there's multiple classes for multiple routes, you'd want a directory/file for keeping all of them together)

from flask import Blueprint, jsonify, abort, make_response

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

# helper function to validate crystal id
def validate_crystal(crystal_id):
    try:
        crystal_id = int(crystal_id)
    except:
        abort(make_response(({"message": f"Crystal {crystal_id} is not a valid input type. ({type(crystal_id)}. Must be an integer.)"}, 400)))
    for crystal in crystals:
        if crystal.id == crystal_id:
            return crystal
    abort(make_response({"message": f"Crystal id {crystal_id} does not exist"}, 404))



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


@crystal_bp.route("/<crystal_id>", methods=["GET"])
def handle_crystal(crystal_id):
    crystal = validate_crystal(crystal_id)
    return {
    "id": crystal.id,
    "name": crystal.name,
    "color": crystal.color,
    "powers": crystal.powers
    }
    
# jsonifying -- only needed when things like lists are returned and need to be formatted in json
