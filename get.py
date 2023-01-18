from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"tim": {"age": 19, "gender": "male"},
         "bill": {"age": 23, "gender": "male"}}


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

    def post(self):
        return {"data": "Posted"}

    def get(self, name):
        return names[name]


api.add_resource(HelloWorld, "/helloworld")

if __name__ == '__main__':
    app.run(debug=True)


