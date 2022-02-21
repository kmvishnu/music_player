from app import app,mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, flash, request
from werkzeug.security import generate_password_hash,check_password_hash

@app.route('/add',methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        id = mongo.db.users.insert_one({'name':_name, 'email':_email, 'password':_hashed_password})
        resp = jsonify("user added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.route('/users')
def users():
    users = mongo.db.users.find()
    resp = dumps(users)
    return resp

@app.route('/users/<id>')       # http://127.0.0.1:5000/users/61f246b81a1a0f6b65747c31
def user(id):                                                # the id of user 
    users = mongo.db.users.find_one({"_id":ObjectId(id)})
    resp = dumps(users)
    return resp

@app.route('/update',methods=['PUT'])
def update_user():
    _json = request.json
    _id = _json['_id']
    _name = _json['name']
    _email = _json['email']
    _password = _json['password']

    if _name and _email and _password and  _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)
        # $oid is key in output from postman
        #http://127.0.0.1:5000/update
        # give the following as input in postman->body->raw and text->json
        #{"_id": {"$oid": "61f246b81a1a0f6b65747c31"}, "name": "john_honaai", "email": "ddasdadasdfsdf", "password": "6vxsd"}
        mongo.db.users.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
        {'$set':{'name':_name,'email':_email,'password':_hashed_password}}) 
        resp = jsonify("User Updated Successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found

@app.route('/user/delete/<id>',methods=["DELETE"])
#the following will delete the corresponding user
#http://127.0.0.1:5000/user/delete/61f246b81a1a0f6b65747c31

def delete_user(id):
    mongo.db.users.delete_one({'_id':ObjectId(id)})
    resp = jsonify("User deleted Successfully")
    resp.status_code = 200
    return resp

@app.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message':'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

if __name__ =="__main__":
    app.run(port=5001)