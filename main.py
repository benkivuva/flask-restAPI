#!/usr/bin/python
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self, name, test):
            return {"name": name, "test": test}

api.add_resource(HelloWorld, "/hellombole/<string:name>/int:test")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
