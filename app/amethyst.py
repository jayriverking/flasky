# this is the routes.py file substitute (if there's multiple classes for multiple routes, you'd want a directory/file for keeping all of them together)
from flask import Blueprint

# Make class Crystal
class Crystal:
    def __init__(self, id, name, color, powers):
        self.id = id
        self.name = name
        self.color = color
        self.powers = powers

# Make Blueprint for an instance of Amethyst

# amethyst_bp = Blueprint("", __name__, url_prefix="")

# @amethyst_bp.routes("/", methods=["GET"])
# def somefunction():