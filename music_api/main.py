from app import app,mongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,flash,request
from werkzeug.security import generate_password_hash,check_password_hash


@app.route('/findmusic')
def findmusic():
    findmusic=mongo.db.MusicData.find()
    resp=dumps(findmusic)
    return resp

if __name__ == "__main__":
    app.run()