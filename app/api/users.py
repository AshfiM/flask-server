from flask import jsonify
from . import users_bp

@users_bp.route("/showusers")
def showUsers():
    return jsonify({"msg":"showusers route"})
