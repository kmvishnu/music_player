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



@app.route('/loginPage',methods=['POST'])
def login_user():
    _json = request.json
    _email = _json["email"]
    _password = _json["password"]

    users = mongo.db.users.find_one({"email":_email})
  
    if  _email and _password and request.method == 'POST':
        if users and check_password_hash(users["password"],_password) :
            resp = jsonify("working great")
            resp.status_code = 200
            return resp
        else:
            return jsonify("wrong details")  
    else:
        return not_found()
       



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