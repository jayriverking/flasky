# this is the routes.py file substitute (if there's multiple classes for multiple routes, you'd want a directory/file for keeping all of them together)
from app import db
from app.models.crystal import Crystal
from flask import Blueprint, jsonify, abort, make_response, request

crystal_bp = Blueprint("crystals", __name__, url_prefix="/crystals")

@crystal_bp.route("", methods=["POST"])
def handle_crystals():
    request_body = request.get_json()
    new_crystal = Crystal(
        name = request_body["name"],
        color = request_body["color"],
        powers = request_body["powers"]
    )
    db.session.add(new_crystal)
    db.session.commit()

    return make_response(f"Crystal {new_crystal.name} successfully created.", 201)
    