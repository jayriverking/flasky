# this is the routes.py file substitute (if there's multiple classes for multiple routes, you'd want a directory/file for keeping all of them together)
from app import db
from app.models.crystal import Crystal
from app.models.healer import Healer
from flask import Blueprint, jsonify, abort, make_response, request

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")
healer_bp = Blueprint("healers", __name__, url_prefix="/healers")

# helper function: validate crystal
def validate_model(cls, model_id):
    # if crystal_id isn't an integer, give back 400 (+ abort mission)
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message": f"{model_id} is invalid"}, 400))
    # query the crystal
    model = cls.query.get(model_id)
    # if it doesn't exist, give back 404 Not Found (+ abort mission)
    if not model:
        abort(make_response({"message": f"{model.__name__} {crystal_id} does not exist"}, 404))
    # return the crystal if it exists!
    return model


@crystal_bp.route("", methods=["POST"])
def make_new_crystal():
    # get data from user
    request_body = request.get_json()
    # make a new crystal using from_dict method
    new_crystal = Crystal.from_dict(request_body)
    # adding to database
    db.session.add(new_crystal)
    # save to database
    db.session.commit()
    # return message and "201 Created" status code
    return jsonify(f"Crystal {new_crystal.name} successfully created."), 201

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
            crystal.to_dict()
        )
    return jsonify(crystal_response)


# define a route for getting a single crystal
# GET /crystals/<crystal_id>
@crystal_bp.route("/<crystal_id>", methods=["GET"])
def read_one_crystal(crystal_id):
    # Query our db
    crystal = validate_crystal(crystal_id)
    return crystal.to_dict()

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



@healer_bp.route("", methods=['POST'])
# define a route for creating a crystal resource
def create_healer():
    request_body = request.get_json()
    
    new_healer = Healer(
        name=request_body["name"]
    )
    
    db.session.add(new_healer)
    db.session.commit()
    
    return jsonify(f"Yayyyy Healer {new_healer.name} successfully created!"), 201


@healer_bp.route("", methods=["GET"])
def read_all_healers():
    
    healers = Healer.query.all()
        
    healers_response = []
    
    for healer in healers:
        healers_response.append({ "name": healer.name})
    
    return jsonify(healers_response)