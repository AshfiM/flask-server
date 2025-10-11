
from flask import Blueprint, jsonify, request, make_response
from app.models import Users, db
from flask_jwt_extended import (create_access_token, 
                                create_refresh_token, 
                                set_access_cookies, 
                                set_refresh_cookies,
                                unset_jwt_cookies, 
                                jwt_required,
                                get_jwt_identity,
                                )

from . import auth_bp

@auth_bp.route("/signup", methods=['POST'])
def signup():
    first_name = request.form.get("first_name")
    email = request.form.get("email")
    password = request.form.get("password")
    
    if Users.query.filter_by(email=email).first():
        return jsonify({"msg":"user already registered"}), 400
    
    user = Users(first_name=first_name, email=email)
    user.setPasswordHash(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg":"user registered"}), 200

@auth_bp.route("/login", methods=['POST'])
def authenticate():
    data = request.get_json(silent=True)
    if not data:
        data = request.form
    email = data.get("email")
    password = data.get("password")
    user = Users.query.filter_by(email=email).first()
    if not user or not user.checkPassword(password):
        return jsonify({"msg":"invalid credentials"}), 401
    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))
    
    resp = make_response(jsonify({"msg":"authenticated"}))
    set_access_cookies(resp, access_token) 
    set_refresh_cookies(resp, refresh_token) 
    
    return resp, 200

@auth_bp.route("/logout", methods=['POST'])
def logout():
    resp = make_response(jsonify({"msg":"logged out"}))
    unset_jwt_cookies(resp)
    return resp, 200

@auth_bp.route("/identity")
@jwt_required()
def identity():
    user = get_jwt_identity()
    return jsonify({"msg":f"user is {user}"}), 200

@auth_bp.route("/refresh", methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    resp = make_response(jsonify({"msg":"access token refreshed"}))
    set_access_cookies(resp, new_access_token)
    return resp, 200



