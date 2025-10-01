from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/auth")
def authenticate():
    return jsonify({"msg":"authenticated"})
