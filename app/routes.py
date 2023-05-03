# this is the routes.py file substitute (if there's multiple classes for multiple routes, you'd want a directory/file for keeping all of them together)
from app import db
from app.models.crystal import Crystal
from flask import Blueprint, jsonify, abort, make_response, request

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

# helper function: validate crystal
def validate_crystal(crystal_id):
    # if crystal_id isn't an integer, give back 400 (+ abort mission)
    try:
        crystal_id = int(crystal_id)
    except:
        abort(make_response({"message": f"{crystal_id} is invalid"}, 400))
    # query the crystal
    crystal = Crystal.query.get(crystal_id)
    # if it doesn't exist, give back 404 Not Found (+ abort mission)
    if not crystal:
        abort(make_response({"message": f"Crystal {crystal_id} does not exist"}, 404))
    # return the crystal if it exists!
    return crystal


@crystal_bp.route("", methods=["POST"])
def make_new_crystal():
    request_body = request.get_json()
    new_crystal = Crystal(
        name = request_body["name"],
        color = request_body["color"],
        powers = request_body["powers"]
    )
    db.session.add(new_crystal)
    db.session.commit()

    return make_response(f"Crystal {new_crystal.name} successfully created.", 201)

# get all crystals!
@crystal_bp.route("", methods=["GET"])
def read_all_crystals():
    color_query = request.args.get("color")
    powers_query = request.args.get("powers")

    if color_query and powers_query:
        crystals = Crystal.query.filter_by(color=color_query, powers=powers_query)
    
    # elif powers_query:
    #     crystals = Crystal.query.filter_by(powers=powers_query)

    else:
        crystals = Crystal.query.all()
    
    crystal_response = []
    for crystal in crystals:
        crystal_response.append(
            {
                "id":crystal.id,
                "name": crystal.name,
                "color": crystal.color,
                "powers": crystal.powers
            }
        )
    return jsonify(crystal_response)


# define a route for getting a single crystal
# GET /crystals/<crystal_id>
@crystal_bp.route("/<crystal_id>", methods=["GET"])
def read_one_crystal(crystal_id):
    # Query our db
    crystal = validate_crystal(crystal_id)
    return {
        "id": crystal.id,
        "name": crystal.name,
        "color": crystal.color,
        "powers": crystal.powers
    }

@crystal_bp.route("/<crystal_id>", methods=["PUT"])
def update_crystal(crystal_id):
    crystal = validate_crystal(crystal_id)
    request_body = request.get_json()
    
    crystal.name = request_body["name"]
    crystal.color = request_body["color"]
    crystal.powers = request_body["powers"]

    db.session.commit()

    return make_response(f"Crystal {crystal.id} successfully updated")

@crystal_bp.route("/<crystal_id>", methods=["DELETE"])
def delete_crystal(crystal_id):
    crystal = validate_crystal(crystal_id)

    db.session.delete(crystal)
    db.session.commit()

    return make_response(f"Crystal {crystal.id} successfully deleted")

