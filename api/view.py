from app import app
from flask import request, jsonify
from models import User
from app import db
from schema import user_schema, users_schema


@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    
    new_user = User(username, email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.dump(new_user)


#show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)


#get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


#update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)