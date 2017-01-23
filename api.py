#!/usr/bin/python
from flask import Flask
from flask_restful import Resource, Api
import math
app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class PiDecimal(Resource):
    def get(self, places):
        pi = math.pi
        # res = "%.2f" % pi
        points = '{:.' + places + 'f}'
        res = points.format(pi)
        return {"%s Decimals" % places: res}

api.add_resource(HelloWorld, '/')
api.add_resource(PiDecimal, '/<string:places>')

if __name__ == '__main__':
    app.run(port=int("46000"), debug=False)




