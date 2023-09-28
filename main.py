#!/usr/bin/python
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"ben": {"age": 34, "gender": "male"}, "mbole": {"age": 43, "gender": "male"}}

class HelloWorld(Resource):
    def get(self, name):
            return names[name]

api.add_resource(HelloWorld, "/hellombole/<string:name>")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
