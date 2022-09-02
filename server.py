from flask import Flask, redirect, url_for, render_template, request
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

try:
    mongo = pymongo.MongoClient(
        host = "localhost",
        port = 27017,
        serverSelectionTimeoutMS = 1000
    )
    db = mongo.company.users
    mongo.server_info()
except:
    print("ERROR - Cannot connect to db")
###########################################

@app.route("/")
def awal():
    return("Selamat datang")

@app.route("/input/sensor")
def data():
    data = request.args.get("data")
    return("nilai adalah {}".format(data))

###########################################
if __name__ == "__main__":
    app.run(port=9090, debug=False,host='0.0.0.0')