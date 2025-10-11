from flask import jsonify
from . import dataSets_bp

@dataSets_bp.route("/showitems")
def showItems():
    return jsonify({"msg":"showitems route"})


